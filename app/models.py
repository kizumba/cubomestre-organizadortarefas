from django.db import models
from django.contrib.auth.models import AbstractUser

SEXO_CHOICES = (
    ("M","Masculino"),
    ("F","Feminino"),
)

STATUS_CHOICES = (
    (0, "Não iniciado"),
    (1, "Em andamento"),
    (2, "Concluído"),
    (3, "Bloqueado"),
    (4, "Cancelado"),
)

class Endereco(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MG", "Minas Gerais"),
        ("MS", "Mato Grosso do Sul"),
        ("MT", "Mato Grosso"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("PR", "Paraná"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("RS", "Rio Grande do Sul"),
        ("SC", "Santa Catarina"),
        ("SE", "Sergipe"),
        ("SP", "São Paulo"),
        ("TO", "Tocantins"),
    )
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    uf = models.CharField(max_length=2, choices=ESTADO_CHOICES, null=False, blank=False)
    cep = models.CharField(max_length=9)
    criado_em = models.DateTimeField(auto_now_add=True)
    modidicado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}"
    

class Cliente(models.Model):
    DOCUMENTO_CHOICES = (
        ("CPF", "CPF"),
        ("CNPJ","CNPJ"),
    )
    PESSOA_CHOICES = (
        ("Física", "Física"),
        ("Jurídica", "Jurídica"),
    )
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    tipo_documento = models.CharField(max_length=4, choices=DOCUMENTO_CHOICES, null=False, blank=False, unique=True)
    tipo_pessoa = models.CharField(max_length=8, choices=PESSOA_CHOICES, null=False, blank=False)
    numero_documento = models.CharField(max_length=14, null=False, blank=False, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    endereco = models.ForeignKey(to=Endereco, on_delete=models.CASCADE, related_name="cliente")

    def __str__(self):
        return f"{self.nome} - {self.tipo_documento}: {self.numero_documento}"
    
class Funcionario(AbstractUser):
    CARGO_CHOICES = (
        (1, "Administrador"),
        (2, "Gerente"),
        (3, "Colaborador")
    )
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    cargo = models.IntegerField(choices=CARGO_CHOICES)
    data_contratacao = models.DateField(auto_now_add=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(to=Endereco, on_delete=models.CASCADE, related_name="funcionario")
    
    habilidades = models.ManyToManyField(
        "Habilidade",
        through="FuncionarioHabilidade",
        through_fields=("colaborador", "habilidade"),
        related_name="funcionarios"
    )

    def __str__(self):
        return f"RA: {self.pk}, Nome: {self.username}, Cargo: {self.get_cargo_display()}"
    
class Habilidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    descricao = models.TextField(null=True, blank=True)
    ativa = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

class FuncionarioHabilidade(models.Model):
    colaborador = models.ForeignKey(to=Funcionario,on_delete=models.CASCADE, null=True)
    habilidade = models.ForeignKey(to=Habilidade, on_delete=models.CASCADE ,null=True)

    class Meta:
        unique_together = ["colaborador", "habilidade"]
    
    def __str__(self):
        return f"{self.colaborador.nome} - {self.habilidade.nome}"
    
    
class Projeto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    descricao = models.TextField(null=False, blank=False)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrega_prevista = models.DateField(null=True, blank=True)
    data_entrega_real = models.DateField(null=True, blank=True)
    is_ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    cliente = models.ForeignKey(to=Cliente, on_delete=models.SET_NULL, related_name="projetos", null=True)
    gerente = models.ForeignKey(to=Funcionario, on_delete=models.SET_NULL, related_name="projetos_gerenciados", null=True)

    def __str__(self):
        return f"{self.nome} - Entrega: {self.data_entrega_prevista}"

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    data_entrega_prevista = models.DateField(null=True, blank=True)
    data_entrega_real = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modidicado_em = models.DateTimeField(auto_now=True)

    projeto = models.ForeignKey(to=Projeto, on_delete=models.CASCADE, related_name="tarefas")
    colaborador = models.ForeignKey(to=Funcionario, on_delete=models.SET_NULL, related_name="tarefas", null=True)
    habilidade = models.ForeignKey(to=Habilidade, on_delete=models.CASCADE, related_name="tarefas")

    def __str__(self):
        return f"{self.nome} - {self.ativa} - {self.get_status_display()}. Responsável: {self.colaborador.username}"
    