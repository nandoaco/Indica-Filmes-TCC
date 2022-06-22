import sqlite3

nome_banco = "filmes.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER , titulo TEXT , imagem TEXT, descrição TEXT
filmes = [
   (1, 'Central do Brasil', 'central do brasil.jpg ', '''Dora, uma amargurada ex-professora, ganha a vida escrevendo cartas para pessoas analfabetas, 
   que ditam o que querem contar às suas famílias. Ela embolsa o dinheiro sem sequer postar as cartas. 
   Um dia, Josué, o filho de nove anos de idade de uma de suas clientes, acaba sozinho quando a mãe é morta em um acidente de ônibus. 
   Ela reluta em cuidar do menino, mas se junta a ele em uma viagem pelo interior do Nordeste em busca do pai de Josué, que ele nunca conheceu.''','https://bit.ly/3bfKZZk','''Data de lançamento: 3 de abril de 1998 (Brasil)
    Diretor: Walter Salles
    Prêmios: Urso de Ouro, Prêmio BAFTA de Cinema: Melhor Filme,Prêmio do Júri Ecumênico entre outros.
    Indicações: Oscar de Melhor Atriz, Urso de Ouro, Prêmio Globo de Ouro: Melhor Filme Estrangeiro ...
    Roteiro: João Emanuel Carneiro, Marcos Bernstein
    Música composta por: Antonio Pinto, Jaques Morelenbaum .
    '''),
   
   (2, 'Bicho de sete cabeças', 'Bicho de sete.jpg ', '''O relacionamento entre Wilson e seu filho Neto está cada vez pior. 
   A situação entre os dois está prestes a chegar ao seu limite, quando o pai decide internar o filho em um manicômio, 
   onde o rapaz enfrenta condições terríveis de tratamento.''', 'https://bit.ly/3Ou9kJ0','''Data de lançamento: 22 de junho de 2001 (Brasil)
    Diretora: Laís Bodanzky
    Autor: Austregésilo Carrano Bueno
    Baseado em: Canto dos Malditos, de Austregésilo Carrano Bueno
    Companhia(s) produtora(s): Buriti Filmes; Dezenove Som e Imagens Produções Ltda. Gullane Filmes; Fabrica Cinema
    Música composta por: André Abujamra, Arnaldo Antunes, Pena Schmidt.
   '''),

   (3, 'O Auto da compadecida', 'o auto da compadecida.jpg', '''As aventuras de João Grilo e Chicó, dois nordestinos pobres que vivem de golpes para sobreviver. 
   Eles estão sempre enganando o povo de um pequeno vilarejo, inclusive o temido cangaceiro Severino de Aracaju, que os persegue pela região.''','https://bit.ly/3Owmgym','''Data de lançamento: 10 de setembro de 2000 (Brasil)
    Diretor: Guel Arraes
    Música: Sá Grama
    Adaptação de: Auto da Compadecida
    Baseado em: Auto da Compadecida; O Santo e a Porca e; Torturas de um Coração, de Ariano Suassuna
    Roteiro: Guel Arraes, Adriana Falcão, João Falcão.
    Elenco: Matheus Nachtergaele, Selton Mello, Rogério Cardoso, Virgínia Cavendish, Fernanda Montenegro, Denise Fraga, Paulo Goulart, Luís Melo, Marco Nanini, Diogo Vilela e Bruno Garcia. 
'''),

   (4, 'Cidade de Deus', 'CidadedeDeus.jpg ', '''Buscapé é um jovem pobre, negro e sensível, que cresce em um universo de muita violência. 
   Ele vive na Cidade de Deus, favela carioca conhecida por ser um dos locais mais violentos do Rio. Amedrontado com a possibilidade de se tornar um bandido, 
   Buscapé é salvo de seu destino por causa de seu talento como fotógrafo, o qual permite que siga carreira na profissão. 
   É por meio de seu olhar atrás da câmera que ele analisa o dia a dia da favela em que vive, onde a violência aparenta ser infinita.''','https://bit.ly/3OqP0rX','''Data de lançamento: 30 de agosto de 2002 (Brasil)
    Diretores: Kátia Lund, Fernando Meirelles
    Adaptação de: Cidade de Deus
    Gênero(s): Samba, rock, soul, funk e MPB
    Lançamento: 2002
    Prêmios: Prêmio BAFTA de Cinema: Melhor Montagem, British Independent Film Award - Melhor filme estrangeiro, Satellite Award de Melhor Filme Estrangeiro,
    Elenco: Kátia Lund, Alexandre Rodrigues, Alice Braga, Douglas Silva, Leandro Firmino, Darlan Cunha, Jefechander Suplino, Seu Jorge, Phellipe Haagensen, Jonathan Haagensen e Roberta Rodrigues.
'''),
  
   (5, 'Malasarte e o duelo contra a morte', 'malasartes.jpg ', '''O jovem Pedro Malasartes é um malandro que viaja de cidade em cidade pregando peças em estranhos desavisados e ingênuos,
    seja para conseguir uma refeição ou para algo que precise em algum momento. Muito inteligente, Malasartes acaba chamando a atenção da Morte, 
    que deseja tirar férias e quer que ele fique em seu lugar. Ele também precisa lidar com Próspero, um homem disposto a fazer de tudo para evitar que o jovem malandro conquiste sua irmã Áurea.''','https://bit.ly/3y4piEw','''Data de lançamento: 10 de agosto de 2017 (Brasil)
    Diretor: Paulo Morelli
    Distribuição: Paris Filmes
    Gênero: aventura; comédia; fantasia
    Indicações: Grande Prêmio do Cinema Brasileiro - Melhor Ator
    Elenco: Jesuíta Barbosa, Isis Valverde, Júlio Andrade, Leandro Hassum, Lima Duarte, Augusto Madeira, Gabriel Sater, Milhem Cortaz, Vera Holtz, Douglas Silva e Julia Ianina.
''')
]
cur.executemany ("INSERT INTO FILMES VALUES(?, ?, ?, ?, ?, ?)", filmes)

con.commit()
con.close()