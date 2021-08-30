import unittest
from Main import Store, Client 

class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Store(15, 0)
        self.c = Client('Bruno',100)

    def testCallOrderComDesconto(self): #1 # CallOrder Sem Desconto
      print("#1 Testar loja recebendo mais de 3 pedidos (Com Desconto)")
      self.assertEqual(self.s.callPayment(4,"Semana",5),1400)

    def testCallOrderSemDesconto(self): #2 # CallOrder Sem Desconto
      print("#2 Testar loja recebendo menos de 3 pedidos (Sem Desconto)")
      self.assertEqual(self.s.callPayment(2,"Dia",4),200)
  
    def testCallOrderAcimaDoEstoque(self): #3 # CallOrder Acima do estoque
      print("#3 Testar loja recebendo acima do estoque")
      self.assertEqual(self.s.callPayment(200,"hora",10),0)

    def testCallOrderPedidoNegativo(self): #4 #CallOrder Pedido Negativo
      print("#4 Testar loja recebendo pedido Negativo")
      self.assertEqual(self.s.callPayment(-1,"hora",10),0)

    def testCallOrderPedidoNegativoNoTempo(self): #5 #CallOrder Pedido Negativo no tempo #5
      print("#5 Testar loja recebendo pedido Negativo no tempo pedido")
      self.assertEqual(self.s.callPayment(1,"hora",-2),0)
    
    def testReceivePayment(self): #1 # payAccount
      print("#6 Testar Pagando aluguel com divida")
      self.assertEqual(self.s.receivePayment(100,90),10)  
    
    def testReceivePayment2(self): #2 # payAccount
      print("#7 Testar Pagando aluguel com divida")
      self.assertEqual(self.s.receivePayment(90,100),10)  

    def testReceivePaymentErrorValue(self): #2 # payAccount
      print("#8 Testar Pagando aluguel com divida")
      self.assertEqual(self.s.receivePayment(-100,100),-1)  

    def testOrderQtdInvalida(self):
      print("#9 Testar loja com quantidade inválida")
      self.assertEqual(self.c.order(-1, "Semana", 1,self.s),-1)

    def testOrderTempoInvalidao(self):
      print("#10 Testar tempo pedido inválida")
      self.assertEqual(self.c.order(1, "Semana", -11,self.s),-1)
    
    def testPlanInvalida(self):
      print("#11 Testar plano inválido")
      self.assertEqual(self.c.order(1, "Weeks", 1,self.s),-1)

    def testOrderOk(self):
      print("#12 Testar Pedido correto")
      self.assertEqual(self.c.order(1, "Semana", 1,self.s),-1)

    def testpayAccount(self): 
      print("#13 Testar Pagando aluguel, pagando certo")
      self.assertEqual(self.c.payAccount(80,self.s),20)

    def testpayAccount(self): 
      print("#14 Testar Pagando aluguel, Pagando com valor negativo")
      self.assertEqual(self.c.payAccount(-80,self.s),-1)

    def testpayAccountError(self): 
      print("#15 Testar Pagando aluguel com divida")
      self.assertEqual(self.c.payAccount(120,self.s),-1)

#receivePayment
if __name__ == "__main__":
    unittest.main()