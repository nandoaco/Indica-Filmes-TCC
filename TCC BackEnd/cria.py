import sqlite3

nome_banco = "filmes.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER , titulo TEXT , imagem TEXT, descrição TEXT
filmes = [
   (1, 'Central do Brasil', 'central do brasil.jpg ', '''Dora, uma amargurada ex-professora, ganha a vida escrevendo cartas para pessoas analfabetas, 
   que ditam o que querem contar às suas famílias. Ela embolsa o dinheiro sem sequer postar as cartas. 
   Um dia, Josué, o filho de nove anos de idade de uma de suas clientes, acaba sozinho quando a mãe é morta em um acidente de ônibus. 
   Ela reluta em cuidar do menino, mas se junta a ele em uma viagem pelo interior do Nordeste em busca do pai de Josué, que ele nunca conheceu.''','https://bit.ly/3bfKZZk'),
   
   (2, 'Bicho de sete cabeças', 'Bicho de sete.jpg ', '''O relacionamento entre Wilson e seu filho Neto está cada vez pior. 
   A situação entre os dois está prestes a chegar ao seu limite, quando o pai decide internar o filho em um manicômio, 
   onde o rapaz enfrenta condições terríveis de tratamento.''', 'https://bit.ly/3Ou9kJ0'),

   (3, 'O Auto da compadecida', 'o auto da compadecida.jpg', '''As aventuras de João Grilo e Chicó, dois nordestinos pobres que vivem de golpes para sobreviver. 
   Eles estão sempre enganando o povo de um pequeno vilarejo, inclusive o temido cangaceiro Severino de Aracaju, que os persegue pela região.''','https://bit.ly/3Owmgym'),

   (4, 'Cidade de Deus', 'CidadedeDeus.jpg ', '''Buscapé é um jovem pobre, negro e sensível, que cresce em um universo de muita violência. 
   Ele vive na Cidade de Deus, favela carioca conhecida por ser um dos locais mais violentos do Rio. Amedrontado com a possibilidade de se tornar um bandido, 
   Buscapé é salvo de seu destino por causa de seu talento como fotógrafo, o qual permite que siga carreira na profissão. 
   É por meio de seu olhar atrás da câmera que ele analisa o dia a dia da favela em que vive, onde a violência aparenta ser infinita.''','https://bit.ly/3OqP0rX'),
  
   (5, 'Malasarte e o duelo contra a morte', 'malasartes.jpg ', '''O jovem Pedro Malasartes é um malandro que viaja de cidade em cidade pregando peças em estranhos desavisados e ingênuos,
    seja para conseguir uma refeição ou para algo que precise em algum momento. Muito inteligente, Malasartes acaba chamando a atenção da Morte, 
    que deseja tirar férias e quer que ele fique em seu lugar. Ele também precisa lidar com Próspero, um homem disposto a fazer de tudo para evitar que o jovem malandro conquiste sua irmã Áurea.''','https://bit.ly/3y4piEw')
]
cur.executemany ("INSERT INTO FILMES VALUES(?, ?, ?, ?, ?)", filmes)

con.commit()
con.close()