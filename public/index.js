async function carregarAutomoveis(){
  const response = await axios.get('http://127.0.0.1:8000/carros')

  const carros = response.data

  const lista = document.getElementById('lista_carros')

  lista.innerHTML= ''

  carros.forEach(carro => { 
    const item = document.createElement('li')
    item.innerText = carro.nome 
  
    lista.appendChild(item)
  });
}


function gravarFormulario() {
  const carro = document.getElementById('form-carro');
  const input_id = document.getElementById('id')
  const input_nome = document.getElementById('nome')
  const input_marca = document.getElementById('marca')
  const input_modelo = document.getElementById('modelo')
  const input_cor = document.getElementById('cor')
  const input_preco = document.getElementById('preco')

  carro.onsubmit = async (event) => {
    event.preventDefault();
    const id = input_id.value
    const nome = input_nome.value
    const marca = input_marca.value
    const modelo = input_modelo.value
    const cor = input_cor.value
    const preco = input_preco.value

    await axios.post('http://127.0.0.1:8000/carros',{
        id: id,
        nome: nome,
        marca: marca,
        modelo: modelo,
        cor: cor,
        preco: preco

  })
    carregarAutomoveis()
    alert('Carro cadastrado com sucesso')
  }
}

function app(){
  console.log('Iniciando api ....') 
  carregarAutomoveis()
  gravarFormulario()
}

document.addEventListener('DOMContentLoaded', app);
