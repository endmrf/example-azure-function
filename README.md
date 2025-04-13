📦 example-azure-function
Este repositório contém um exemplo de Azure Function escrita em Python, com o objetivo de estudar recursos serverless na plataforma Azure.​

🚀 Requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados:

Python 3.8+​

Azure Functions Core Tools​

Azure CLI​

Visual Studio Code com a extensão Azure Functions (opcional, mas recomendado)​

🛠️ Configuração do Projeto
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/endmrf/example-azure-function.git
cd example-azure-function
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Inicie a função localmente:

bash
Copiar
Editar
func start
A função estará disponível em http://localhost:7071/api/<nome-da-função>.

📁 Estrutura do Projeto
function_app.py: Código principal da Azure Function.​
GitHub
+5
GitHub
+5
GitHub
+5

host.json: Configurações do host da função.​
GitHub

requirements.txt: Lista de dependências Python.​
GitHub

.funcignore: Arquivos e pastas ignorados pelo Azure Functions Core Tools.​
GitHub
+2
GitHub
+2
GitHub
+2

.vscode/: Configurações para o Visual Studio Code.​

.github/workflows/: Configurações de integração contínua (CI) com GitHub Actions.​

☁️ Publicação no Azure
Para implantar a função no Azure:

Efetue login no Azure:

bash
Copiar
Editar
az login
Crie um grupo de recursos e uma conta de armazenamento:

bash
Copiar
Editar
az group create --name myResourceGroup --location brazilsouth
az storage account create --name mystorageaccount --location brazilsouth --resource-group myResourceGroup --sku Standard_LRS
Crie o plano de hospedagem e a Function App:

bash
Copiar
Editar
az functionapp plan create --resource-group myResourceGroup --name myFunctionPlan --location brazilsouth --number-of-workers 1 --sku B1 --is-linux
az functionapp create --resource-group myResourceGroup --consumption-plan-location brazilsouth --runtime python --runtime-version 3.8 --functions-version 3 --name myFunctionApp --storage-account mystorageaccount
Implante a função:

bash
Copiar
Editar
func azure functionapp publish myFunctionApp
📚 Referências
Documentação oficial do Azure Functions​

Azure Functions Core Tools​
GitHub
+2
GitHub
+2
GitHub
+2

Exemplos de Azure Functions em Python​
GitHub
+2
GitHub
+2
GitHub
+2
