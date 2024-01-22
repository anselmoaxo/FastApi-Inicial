

async function carregarAutomoveis(){
  const response = await axios.get('http://127.0.0.1:8000/carros')

  console.log(response.data)


}

function app(){
  console.log('Inciando api ....')
  carregarAutomoveis()
}

app()