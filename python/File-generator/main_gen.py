import atp_wta_gen 
import torneios_atuais_gen 
import resultados_gen
import torneios_individuais_gen

def main():

    #Gerador de ATP, WTA, Torneios Atuais, Resultados, Página dos Torneios

    atp_wta_gen.comp_html('atp')
    atp_wta_gen.comp_html('wta')

    torneios_atuais_gen.torneio_atuais()
    resultados_gen.resultados()

    torneios_individuais_gen.torneios_individuais()

    #Falta criar uma página só com as predicts maybe#

    return None

main()