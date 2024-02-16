# PDF
  
Módulo para realizar ações com arquivos PDF  

*Read this in other languages: [English](Manual_PDF.md), [Português](Manual_PDF.pr.md), [Español](Manual_PDF.es.md)*
  
![banner](imgs/Banner_PDF.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Dividir PDF
  
Esse comando permite dividir um arquivo PDF em vários arquivos PDF com um determinado número de páginas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o PDF|Caminho para o arquivo PDF a ser dividido.|C:/Users/User/Downloads/sample.pdf|
|Caminho da pasta onde salvar os PDFs resultantes|Caminho a ser usado para salvar os PDFs resultantes.|C:/Users/User/Desktop/PDF|
|A cada poucas páginas dividir o PDF|Número de páginas em que o ritmo será definido para dividir o PDF.|1|

### Dividir o PDF em páginas específicas
  
Dividir um PDF em uma etapa específica.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o PDF|Caminho para o arquivo PDF que você deseja dividir.|C:/Users/User/Downloads/sample.pdf|
|Caminho da pasta onde salvar o PDF|Caminho a ser usado para salvar os PDFs resultantes.|C:/Users/User/Desktop/PDF|
|Como dividir o PDF|Passos em que o PDF será dividido.|['1-3', '4-5']|

### Combinar PDFs
  
Esse comando permite combinar vários PDFs de uma pasta em um único PDF.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho da pasta com pdfs|Caminho que contém todos os PDFs para combinar.|C:/Users/User/Desktop/PDF|
|Caminho para usar para salvar o PDF resultante|Caminho para usar para salvar o PDF resultante.|C:/Users/User/Desktop/PDF/merge.pdf|

### Encriptar PDF
  
Esse comando permite adicionar uma senha a um arquivo PDF.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|PDF para encriptar|Caminho para o PDF que você deseja encriptar.|C:/Users/User/Downloads/sample.pdf|
|Caminho e nome do arquivo onde salvar o PDF encriptado|Caminho para usar para salvar o PDF resultante.|C:/Users/User/Downloads/sample.pdf|
|Senha|Senha que o PDF encriptado terá.|s3cr3t-p4ss|

### Desencriptar PDF
  
Este comando permite desencriptar um arquivo PDF.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|PDF encriptado|Caminho onde o PDF encriptado está localizado.|C:/Users/User/Downloads/sample.pdf|
|Senha|Senha para desencriptar o PDF.|s3cr3t-p4ss|
|Salvar PDF desencriptado|Caminho onde o PDF desencriptado será salvo.|C:/Users/User/Downloads/output.pdf|

### Ler PDF
  
Este comando permite ler um PDF. Se o PDF estiver encriptado, fornecendo a senha, ele será descriptografado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|PDF para ler|Caminho onde o PDF está localizado.|C:/Users/User/Downloads/sample.pdf|
|Opção de leitura|Opção de leitura do PDF. Cada opção usa um método diferente para ler o PDF.|1|
|Página/s|Páginas do documento PDF para ler.|1,3,5|
|Retornar em formato lista de dicionário|Se selecionado, o resultado será retornado em formato de lista de dicionários, onde cada um terá a página e o conteúdo.|True|
|Senha|Senha para descriptografar o PDF.|s3cr3t-p4ss|
|Atribuir resultado à variável|Variável para salvar o resultado da leitura do PDF.|pdf_lido|

### Ler caixas de texto e caixas de seleção em PDF
  
Este comando lê as caixas de texto e caixas de seleção de um arquivo PDF.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo PDF|Caminho para o arquivo PDF a ser lido.|C:/Users/User/Downloads/sample.pdf|
|Variável para armazenar o resultado|Variável para armazenar o resultado da leitura do PDF.|resultado|

### Contar Páginas
  
Este comando permite contar as páginas de um PDF.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|PDF para ler|Caminho onde o PDF está localizado.|C:/Users/User/Downloads/sample.pdf|
|Atribuir resultado a variável |Variável onde será salvada a quantidade de páginas do PDF.|nro_pag|

### Escrever em input de PDF
  
Este comando permite escrever em um input de PDF, criando um novo PDF com os dados carregados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo PDF|Caminho para o arquivo PDF a ser lido.|C:/Users/User/Downloads/sample.pdf|
|Dicionário de inputs|Dicionário de inputs do PDF.|{key1:valor1, key2:valor2}|
|Nome do PDF com os dados carregados|Nome e caminho do PDF que será criado com os dados carregados.|C:/Users/User/Downloads/result.pdf|

### Cortar imagem de PDF
  
Crie uma imagem a partir das coordenadas atribuídas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|PDF de entrada|Arquivo PDF que será usado no módulo|arquivo.pdf|
|imagem JPG|Caminho e nome que a imagem JPG extraída do PDF terá|path/imagem.jpg|
|Página|Número da página do PDF de onde a imagem será obtida|3|
|Coordenadas de início|Coordenadas de onde a imagem será obtida|0,0|
|Coordenadas finais|Coordenadas para onde a imagem será obtida|1000,1000|
|DPI|DPI ou Pontos por polegada que a imagem terá. O padrão é 150 DPI|150|

### Converter para JPG
  
Converter cada folha de um arquivo PDF para o formato JPG
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Inserir PDF|Localização da pasta onde se encontra o PDF a converter para JPG|arquivo.pdf|
|Caminho e nome do arquivo JPG para salvar|Local e nome do arquivo JPG a ser salvo. Se o PDF contiver mais de uma folha, o número da folha será adicionado aos arquivos|C:/Users/User/Desktop/imagem.jpg|
|Ancho de imagen|Valor numérico que representará a largura da imagem em pixels.|1500|
|DPI|DPI ou Pontos por polegada que a imagem terá. O padrão é 150 DPI|150|
|Resultado|Variável onde será armazenado True ou False dependendo se o módulo foi capaz de executar a ação|variável|

