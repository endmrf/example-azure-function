# 📦 example-azure-function

Este repositório contém um exemplo de Azure Function escrita em Python, com o objetivo de estudar recursos serverless na plataforma Azure.

## 🚀 Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- [Azure Functions Core Tools](https://learn.microsoft.com/pt-br/azure/azure-functions/functions-run-local)
- [Azure CLI](https://learn.microsoft.com/pt-br/cli/azure/install-azure-cli)
- [Visual Studio Code](https://code.visualstudio.com/) com a extensão [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) (opcional, mas recomendado)

## 🛠️ Configuração do Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/endmrf/example-azure-function.git
   cd example-azure-function

2. **Crie e ative um ambiente virtual:**
  
   ```bash
   python -m venv .venv
   source .venv/bin/activate

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

4. **Inicie a função localmente**:
   ```bash
   func start

A função estará disponível em http://localhost:7071/api/movies.

## 📁 Estrutura do Projeto
- `function_app.py`: Código principal da Azure Function.
- `host.json`: Configurações do host da função.
- `requirements.txt`: Lista de dependências Python.
- `.funcignore`: Arquivos e pastas ignorados pelo Azure Functions Core Tools.
- `.vscode/`: Configurações para o Visual Studio Code.
- `.github/workflows/`: Configurações de integração contínua (CI) com GitHub Actions.

## ☁️ Publicação no Azure
Para implantar a função no Azure:

1. **Efetue login no Azure**:

   ```bash
   az login

2. **Crie um grupo de recursos e uma conta de armazenamento**:

   ```bash
   az group create --name myResourceGroup --location brazilsouth
   az storage account create --name mystorageaccount --location brazilsouth --resource-group myResourceGroup --sku Standard_LRS

3. **Crie o plano de hospedagem e a Function App**:

   ```bash
   az functionapp plan create --resource-group myResourceGroup --name myFunctionPlan --location brazilsouth --number-of-workers 1 --sku B1 --is-linux
   az functionapp create --resource-group myResourceGroup --consumption-plan-location brazilsouth --runtime python --runtime-version 3.8 --functions-version 3 --name myFunctionApp --storage-account mystorageaccount
   
4. **Implante a função**:

    ```bash
    func azure functionapp publish myFunctionApp
    
## 📚 Referências

- [Documentação oficial do Azure Functions](https://learn.microsoft.com/pt-br/azure/azure-functions/)
- ​[Azure Functions Core Tools​](https://learn.microsoft.com/pt-br/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)
- [Exemplos de Azure Functions em Python​](https://github.com/yokawasa/azure-functions-python-samples)
