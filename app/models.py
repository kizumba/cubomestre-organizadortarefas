from django.db import models


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

class Contato(models.Model):
    telefone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.telefone} - {self.email}"
    

class TipoCliente(models.Model):
    PESSOA_CHOICES = (
        ("Jurídica", "Jurídica"),
        ("Física", "Física"),
    )
    pessoa = models.CharField(max_length=8, choices=PESSOA_CHOICES, null=False, blank=False)
    descricao = models.TextField()

class Cliente(models.Model):
    DOCUMENTO_CHOICES = (
        ("CPF", "CPF"),
        ("CNPJ","CNPJ"),
    )
    documento = models.CharField(max_length=14, choices=DOCUMENTO_CHOICES, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    contato = models.ForeignKey(to=Contato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.documento}"
    

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
    titular = models.ForeignKey(to=Cliente, on_delete=models.CASCADE, related_name="endereco")

class TipoFuncionario(models.Model):
    FUNCAO_CHOICES = (
        ("Administrador", "Administrador"),
        ("Gerente", "Gerente"),
        ("Colaborador", "Colaborador"),
    )
    funcao = models.CharField(max_length=13, choices=FUNCAO_CHOICES, null=False, blank=False)
    descricao = models.TextField()

    def __str__(self):
        return self.funcao

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    modidicado_em = models.DateTimeField(auto_now=True)

    contato = models.ForeignKey(to=Contato, on_delete=models.CASCADE)

    habilidades = models.ManyToManyField(
        "Habilidade",
        through="FuncionarioHabilidade",
        through_fields=("funcionario", "habilidade"),
        related_name="funcionarios"
    )

    def __str__(self):
        return f"RA: {self.pk}, Nome: {self.nome}"
    
class Habilidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modidicado_em = models.DateTimeField(auto_now=True)

class FuncionarioHabilidade(models.Model):
    colaborador = models.ForeignKey(to=Funcionario,on_delete=models.CASCADE, null=True)
    habilidade = models.ForeignKey(to=Habilidade, on_delete=models.CASCADE ,null=True)

    class Meta:
        unique_together = ["colaborador", "habilidade"]
    
class Projeto(models.Model):
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrega_prevista = models.DateField(null=True, blank=True)
    data_entrega_real = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modidicado_em = models.DateTimeField(auto_now=True)

    cliente = models.ForeignKey(to=Cliente, on_delete=models.SET_NULL, related_name="projetos", null=True)
    gerente = models.ForeignKey(to=Funcionario, on_delete=models.SET_NULL, related_name="projetos_gerenciados", null=True)

    def __str__(self):
        return f"{self.nome} - {self.data_entrega_prevista}"

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
    colaborador = models.ForeignKey(to=Funcionario, on_delete=models.SET_NULL, related_name="tarefas")
    habilidade = models.ForeignKey(to=Habilidade, on_delete=models.CASCADE, related_name="tarefas")

    def __str__(self):
        return f"{self.nome} - {self.ativa} - {self.status}"
    