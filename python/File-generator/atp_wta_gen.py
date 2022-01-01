import pandas as pd
import extra_functions as ef
from extra_data import excel_path

#Gera a página ATP e WTA

def comp_html(comp):
    f = open(f'{comp}.html','w')
    df = pd.read_excel(io = excel_path, sheet_name = f"{comp.upper()} - Torneios")
    torneios = ef.dic_torneios(ef.dataframe_to_list(df), comp)

    lista = ""
    if len(torneios) != 0:
        for t in dict.keys(torneios):
            lista += ef.torneio_html(torneios[t])
        lista_html = f"""
        <div>
        <ul class="torneios">
        {lista}
        </ul>
        </div>
        """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{comp.upper()}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/main.css">
    </head>
    <body>
        <div id="nav-placeholder"></div>
            <script>$(function(){{$("#nav-placeholder").load("nav.html");}});</script>
            <div class="big-logo">
        <div class="container">
            <h1 class="titulo">Circuito <span>{comp.upper()}</span></h1>
        </div>        
    </div>
        {lista_html}
    </body>
    """

    f.write(full_html)
    f.close()

    print(f'{comp.upper()}: atualizado')