# Sample Swagger Flask Code

Este é um exemplo de código Flask com integração ao Swagger. Ele demonstra como criar uma API utilizando Flask-RestX e documentar os endpoints com Swagger.

## O que é Swagger?

Swagger é uma ferramenta de código aberto amplamente utilizada para projetar, construir, documentar e consumir serviços da web RESTful. Ele fornece uma maneira fácil e padronizada de descrever, definir e visualizar APIs, permitindo a interação com a API sem a necessidade de escrever código adicional.

## Como executar o código

1. Certifique-se de ter o Python instalado no seu ambiente.
2. Instale as dependências e crie o ambinete de desenvolvimento executando o comando `init_venv.bat`.
3. Execute o código usando o comando `python swagger.py`.
4. A aplicação será executada em `http://localhost:5000/`.

## Endpoints

### GET /

Este endpoint retorna uma mensagem de boas-vindas.

### GET /person

Este endpoint retorna informações sobre uma pessoa.

#### Response

```json
{
  "id": 1,
  "name": "João",
  "age": "25"
}
```

## Swagger UI

Após iniciar a aplicação, você pode acessar a interface do Swagger UI em `http://localhost:5000/`. Lá, você encontrará a documentação completa da API, incluindo detalhes sobre os endpoints, parâmetros, modelos de dados e exemplos de resposta.

## Notas adicionais

Certifique-se de ler e entender completamente o código fornecido para personalizar e adaptar de acordo com as suas necessidades. O código demonstra como criar endpoints, definir modelos de dados e integrar o Swagger para documentar a API.

Lembre-se de que o Swagger é uma ferramenta poderosa para documentação e interação com APIs, e é altamente recomendado utilizá-la para melhorar a compreensão e a usabilidade da API.