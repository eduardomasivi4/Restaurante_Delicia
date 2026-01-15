# Restaurante_Delicia

Problema: 
    Atualmente, muitos restaurantes locais enfrentam dificuldades em divulgar seus serviços online, organizar o cardápio e gerir reservas de mesas de forma eficiente. Grande parte desses estabelecimentos depende apenas de redes sociais ou atendimento presencial, o que limita o alcance do negócio e causa desorganização no processo de reservas.
    Um restaurante pretende modernizar sua presença digital através da criação de um sistema web desenvolvido em Django, com um layout moderno inspirado em um template profissional da plataforma Wix (template de restaurante), mantendo identidade visual atrativa e navegação intuitiva.

                OBS: Para este projeto estou a usar o Linux

1º passo:
    Criar o ambiente virtual e as ferramentas necessárias para a criação do projeto:
        Crie uma pasta com o nome do projeto;

        Ambiente virtual: python3 -m venv venv (pode ou não ser necessário)
        Django: pip install djago;
    
    Criar o núcleo do projeto: django-admin startproject core . (O ponto é para indicar que está no diretorio atual)

    Criar as aplicações: 
        1- Comum: para as páginas Home, Sobre, Contactos.
            python3 manage.py startapp comum
        
        2- Menu: para o cardápio.
            python3 manage.py startapp menu
        
        3- Reservas: para as reservas.
            python3 manage.py startapp reservas
        
        4- Contas: para as contas.
            python3 manage.py startapp contas

