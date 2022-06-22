
const tabela= document.querySelector("#tabela-filmes");


function carregarDados(){
    fetch('http://127.0.0.1:5000/todos')
       .then(function(resposta){
        return resposta.json();
       })
    
        .then(function(ListaFilmes){
         popularTabela(ListaFilmes);
    })
}
carregarDados();
 function popularTabela(ListaFilmes){
    console.log(ListaFilmes);
    const tamanhoLista = ListaFilmes.length;
    
     for(let index = 0; index < tamanhoLista; index ++){
        const linha = document.createElement('tr');

        //  const id = document.createElement('td');
         const titulo = document.createElement('td');
         const imagem = document.createElement('td');
         const sinopse= document.createElement('td');

        //  id.innerHTML = ListaFilmes[index][0];
         titulo.innerHTML = ListaFilmes[index][1]
        //  imagem.innerHTML = ListaFilmes[index][2];
         sinopse.innerHTML = ListaFilmes[index][3];

         const link = document.createElement('a');
         link.setAttribute('href', ListaFilmes[index][4]);
         link.setAttribute('target', '_blank');

         const img = document.createElement('img');
         img.setAttribute('src','./' + ListaFilmes[index][2]);

         link.appendChild(img);
        
        //  linha.appendChild(id);
         linha.appendChild(titulo);
         linha.appendChild(link);
         linha.appendChild(sinopse);
         

         tabela.appendChild(linha);
       
        
     }
 }