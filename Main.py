class Client(object):
    def __init__(self, name, wallet):  
        self.name = name
        self.wallet = wallet
        self.account = 0.0
        
    def order(self, item, plan, period, objStore): 
        try:
            if item <= 0 and period > 0:
                raise ValueError("Quantidade invalida")     
            if plan != "Semana" or plan != "Dia" or plan != "Hora":
                raise SyntaxError("O plano está inválido. Precisa escolher plano existentes. Entre: Semana, Dia e Hora")
            if not isinstance(objStore, Store):
                raise SystemError("Não está em uma loja válida")
            
            self.account += objStore.callPayment(item, plan, period)
            print(f"Cliente {self.name} - pedido de {item} bicicletas no periodo de {period}{plan} executado.Conta: R${self.account}")
            return self.account
        except ValueError:
                print(f"Cliente {self.name} - pedido de {item} bicicletas não executado, por quantidade inválida.Conta: R${self.account}")
                return -1
        except SyntaxError:
                print(f"Cliente {self.name} - pedido de {item} bicicletas não executado, por plano inválido.Conta: R${self.account}")
                return -1
        except SystemError:
                print(f"Cliente {self.name} - pedido de {item} bicicletas não executado, por loja inválida.Conta: R${self.account}")
                return -1
        except:
                print(f"Cliente {self.name} - pedido de {item} bicicletas não executado.Conta: R${self.account}")
                return -1

    def payAccount(self, payment, objStore):
        try:
            if payment <= 0:
                raise ValueError("Valor inválido")
            if payment > self.wallet:
                raise ArithmeticError("Pagamento maior que o saldo em carteira")
            if not isinstance(objStore, Store):
                raise SystemError("Não está em uma loja válida") 

            self.wallet -= payment
            due = objStore.receivePayment(self.account, payment)
            print(f"Cliente {self.name} - Com o pagamento de R${payment} o saldo a pagar é R${self.account}. Carteira: R${self.wallet}")
            if due == 0:
                self.account = 0 
            elif due > 0:
                self.account = due
            else:
                self.account -= due   
                self.account = 0
            return self.wallet

        except ValueError:
                print(f"Cliente {self.name} - Com o pagamento de R${payment} o saldo a pagar é R${self.account}. Não efetuado, pois o valor de pagamento não é válido. Carteira: R${self.wallet}")
                return -1 
        except ArithmeticError:
                print(f"Cliente {self.name} - Pagamento inválido: O saldo da carteira R${self.wallet} é inferior ao valor do pedido R${payment}. ")
                return -1                            
        except SystemError:
                print(f"Cliente {self.name} - Com o pagamento de R${payment} o saldo a pagar é R${self.account}. Não efetuado, pois a loja não é válida.Carteira: R${self.wallet}")
                return -1
        except:
                print(f"Cliente {self.name} - Com o pagamento de R${payment} o saldo a pagar é R${self.account}. Não efetuado. Carteira: R${self.wallet}")
                return -1

class Store(object):
    def __init__(self, stock,checkout):
        self.stock = stock
        self.checkout = checkout

    def callPayment(self, item, plan, period): ## calculator
        try:
            if item <= 0:
              raise ZeroDivisionError(f"Quantidade invalida, não é possivel realizar o pedido")

            if self.stock < item:
                raise ValueError(f"Quantidade invalida, sem estoque de bicicleta. Atualmete temos {item}, gostaria de alugar essa(s) bicicleta(s) ")

            self.stock -= item
            discount = 1-0.3
            if plan == "Semana":
                price = 100
            elif plan == "Dia":
                price = 25
            elif plan == "Hora":
                price = 5

            totalOrder = price * item * period
            if item >= 3:
                totalOrder = totalOrder * discount

            print(f"Bicicletário - Pedido de {item} bicicleta(s) feito(s). Alugar bicicletas por {plan} (R${price}/{plan}) ")
            return totalOrder

        except ZeroDivisionError:
            print(f"Bicicletário - Pedido de {item} bicicleta não efetuado por quantidade invalida. Estoque:{self.stock}. ")
            return 0 
        except ValueError:
            print(f"Bicicletário - Pedido de {item} bicicleta não efetuado por falta de estoque. Estoque:{self.stock}. ")
            return 0     
        except SystemError:  
            print(f"Bicicletário - Pedido de {item} bicicleta não efetuado por não encontrar o pedido. Estoque:{self.stock}. ")
            return 0 
        except:
            print(f"Bicicletário - Pedido de {item} bicicleta não efetuado. Estoque:{self.stock}. ")
            return 0       
            
    def receivePayment(self, invoice, payment ):
      try:
          if invoice <= 0 or payment <= 0:
            raise ValueError("Valor(es) invalido(s)")

          if invoice == payment:
            self.checkout += payment
            print(f"Bicicletário - Conta paga totalmente, valor recebido R${payment}, conta R${invoice}. Caixa:{self.checkout}")
            return 0
          elif invoice < payment:
            self.checkout += invoice
            change = payment - invoice 
            print(f"Bicicletário - Conta paga totalmente com troco de R${change}. Valor recebido R${payment}, Conta R${invoice }. Caixa:{self.checkout}")
            return change
          else:
            self.checkout += payment     
            tranche = invoice - payment 
            print(f"Bicicletário - Conta paga parcialmente, restam pagar na devolução R${tranche}. Valor recebido R${payment}, Conta R${invoice}. Caixa:{self.checkout}")
            return tranche

      except ValueError:
          print(f"Bicicletário - Erro ao pagar conta, valor(es) invalido(s).Valor recebido R${payment}, Conta R${invoice }. Caixa:{self.checkout}")
          return -1
      except:
            print(f"Bicicletário - Erro ao pagar conta.Valor recebido R${payment}, Conta R${invoice}. Caixa:{self.checkout}")
            return invoice 