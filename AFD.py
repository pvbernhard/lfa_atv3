from typing import Optional, Dict, Any


class Estado:  
  def configura(self, estados_possiveis: Dict[str, Any]) -> None:
    self.estados_possiveis = estados_possiveis
  
  def proximo(self, caractere: str) -> Optional[Any]:
    if caractere in self.estados_possiveis:
      return self.estados_possiveis[caractere]
    else:
      return None

class MaquinaEstados:
  def __init__(self, estado_inicial: Estado, estado_final: Estado):
    self.estado_inicial = estado_inicial
    self.estado_final = estado_final
  
  def ler(self, palavra: str) -> bool:
    estado = self.estado_inicial
    for c in palavra:
      estado = estado.proximo(c)
      if estado is None:
        return False
    if estado == self.estado_final:
      return True
    else:
      return False


estado_0 = Estado('estado_0')
estado_1 = Estado('estado_1')
estado_2 = Estado('estado_2')

estado_0.configura({'a': estado_0, 'b': estado_1})
estado_1.configura({'b': estado_2})
estado_2.configura({'c': estado_1})

maquina_estados = MaquinaEstados(estado_inicial=estado_0, estado_final=estado_2)

while(True):
    palavra = input('Digite uma palavra:')
    if palavra == '':
      break
    resultado = maquina_estados.ler(palavra)
    if resultado:
        print('aceita')
    else:
        print('rejeita')
    print()
