from clientes import Cliente
from contas import ContaEspecial

pedro = Cliente("Pedro", "1111-1111")
ana = Cliente("Ana", "2222-2222")

c1 = ContaEspecial([pedro], 1, 1000, 1500)
c1.extrato()

c2 = ContaEspecial([ana], 2, 5000, 6000)
c2.extrato()