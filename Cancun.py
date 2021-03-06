import streamlit as st
st.markdown('<p class="font1"> 1..2..3..Cancun ! </p>', unsafe_allow_html=True)


st.markdown(""" <style>

.font1 {

        font-size:60px ;

        font-family: 'Times new roman';

        color: #0689a8;

        text-align: center;

        
        }

.font2 {

        font-size:20px ;

        font-family: 'Times new roman';

        color: #0689a8;

        text-align: right;
        font-weight: bold;
       
}

 
.font3 {

        font-size:20px ;

        font-family: 'times new roman';

        color: red;

        text-align: center;


  }
  
  .font4 {
        font-size:20px ;
        
        font-family: 'Times new roman';
        
        color: green;
        
        text-align: center;
       
}
.font5 {
        font-size:20px ;
        
        font-family: 'Times new roman';
        
        color: black;
        
        text-align: left;

</style> """, unsafe_allow_html=True)




import numpy as np


from PIL import Image
image = Image.open('Cancun.png')

st.image(image, output_format="JPEG")

st.markdown(f'<p class="font5"> -Ton équipe sest fait éliminé des Playoffs 2022 ? Ce nest pas grave ! Fait comme LeBron et les Lakers et part vers la destination numéro 1 des athlètes de la NBA qui ne se rendent pas loin dans la postseason, Cancun ! </p>', unsafe_allow_html=True)

audio_file = open('1, 2, 3... Cancun!.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg', start_time=8)

st.markdown(f'<p class="font5"> -Ce programme permet de calculer les différents revenus et coûts dexploitation pour le vol davion en direction de Cancun. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> Pour utiliser ce programme, il faut rentrer les différentes données concernant le vol. </p>', unsafe_allow_html=True)

st.write()
class Vol_avion:                                            
    """ Cette classe permet de créer différents vols d'avions.""" 
    cf = 40000    #Coûts fixes pour un vol d'avion pour l'entreprise d'aviation
    gaz = 12      #Coûts pour un litre de carburant en dollar
    cv = 162      #Coûts variables en dollar par personne occupant une place dans l'avion
    rr = 5        #Revenus pour l'entreprise d'aviation par repas vendus
    cc = 7        #Coûts reliés au chauffage ou à la climatisation de l'avion lors du vol    
    fe = 2        #Frais reliés à l'entreposage des bagages des passagers par livres  
    
    def __init__(self, distance, passagers, conditions_météo, repas, bagages, prix_billet):          
        """Initialiser les attributs pour calculer les dépenses et revenus d'un vol d'avion."""
        self.distance = distance                            #Distance parcouru lors du vol
        self.passagers = passagers                          #Nombre de passagers à bord de l'avion
        self.conditions_météo = conditions_météo            #Conditions météo lors du vol
        self.repas = repas                                  #Nombre de repas pris par les passagers
        self.bagages = bagages                              #Poids moyen des bagages des passagers
        self.prix_billet = prix_billet                      #Prix de vente d'un billet pour le vol
        
    def couts_passager(self):                                
        """Calcul les coûts reliés à l'occupation des places dans l'avion par les passagers."""
        return self.passagers * Vol_avion.cv
    
    def couts_bagages(self):
        """Calcul les coûts reliés à l'entreprosage des bagages des passagers dans l'avion."""
        return self.passagers * self.bagages * Vol_avion.fe
    
    def couts_carburant_météo(self):
        """Calcul comment les conditions météorologiques affectent la consommation de carburant pour le vol.
        self.distance * Vol_avion.gaz calcul la consommation de carburant avant de prendre en considération la météo."""
        if self.conditions_météo == "excellentes":
            return self.distance * Vol_avion.gaz * 0.80
        
        elif self.conditions_météo == "bonnes":
            return self.distance * Vol_avion.gaz * 0.95
        
        elif self.conditions_météo == "normales":
            return self.distance * Vol_avion.gaz * 1
        
        elif self.conditions_météo == "mauvaises":
            return self.distance * Vol_avion.gaz * 1.05    
        
        elif self.conditions_météo == "très mauvaises":
            return self.distance * Vol_avion.gaz * 1.20    
                
    def couts_chauffage_climatisation(self):
        """Calcul les coûts reliés au chauffage et à la climatisation à l'intérieur de l'avion lors du vol."""
        return self.distance * Vol_avion.cc
    
    def revenus_repas(self):
        """Calcul les ventes de repas lors du vol."""
        return self.repas * Vol_avion.rr
    
    def revenus_billets(self):
        """Calcul les ventes réalisées selon le nombre de billet d'avion vendus pour le vol."""
        return self.passagers * self.prix_billet
    
    def revenus_exploitation_total(self):
        """Calcul les revenus d'exploitation total pour le vol."""
        return Vol_avion.revenus_repas(self) + Vol_avion.revenus_billets(self)
        
    def couts_totaux(self):
        """Calcul les coûts totaux engagés pour exploiter l'avion lors du vol."""
        return Vol_avion.cf + Vol_avion.couts_passager(self) + Vol_avion.couts_bagages(self) + Vol_avion.couts_carburant_météo(self) + Vol_avion.couts_chauffage_climatisation(self)
        
    def benefices(self):   
        """Calcul le bénéfice total ou la perte totale pour l'exploitation de l'avion lors du vol."""
        return Vol_avion.revenus_exploitation_total(self) - Vol_avion.couts_totaux(self)


distance = st.sidebar.number_input('Inserez une distance', step = 1)
passagers = st.sidebar.number_input('Inserez le nombre de passagers', step = 1)
conditions_météo = st.sidebar.selectbox(
     'Quelle était la condition météo pour le calcul de la consommation de carburant lors du vol ?',
     ("excellentes","bonnes","normales","mauvaises","très mauvaises"))
repas = st.sidebar.number_input('Inserez le nombre de repas vendu lors du vol.', step = 1)
bagages = st.sidebar.number_input('Inserez le poids moyen des bagages par passager (en livre)')
prix_billet = st.sidebar.number_input("Inserez le prix pour un billet d'avion.")


vol_Cancun = Vol_avion(distance, passagers, conditions_météo, repas, bagages, prix_billet)

#format(round...), ',d').replace(',',' ')) %d %e %f %g %i %u


st.markdown(f'<p class="font5"> -Les coûts reliés à occupation des places dans avion par les passagers sont de : </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2"> {round(vol_Cancun.couts_passager(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les coûts reliés à lentreprosage des bagages des passagers dans lavion sont de : </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2"> {round(vol_Cancun.couts_bagages(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les coûts de carburant reliés aux conditions météorologique lors du vol sont de : </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2">  {round(vol_Cancun.couts_carburant_météo(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les coûts reliés au chauffage et à la climatisation à lintérieur de lavion lors du vol sont de :  </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2">  {round(vol_Cancun.couts_chauffage_climatisation(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les profits générés par la vente de repas lors du vol sont de :  </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2">  {round(vol_Cancun.revenus_repas(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les profits générés par la vente de billets davion pour le vol sont de : </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2"> {round(vol_Cancun.revenus_billets(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les revenus dexploitation total pour le vol sont de : . </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2">  {round(vol_Cancun.revenus_exploitation_total(), 2)} $. </p>', unsafe_allow_html=True)

st.markdown(f'<p class="font5"> -Les coûts totaux réliés à lexploitation de lavion pour le vol sont de :  </p>', unsafe_allow_html=True)
st.markdown(f'<p class="font2">  {round(vol_Cancun.couts_totaux(), 2)} $. </p>', unsafe_allow_html=True)
if vol_Cancun.benefices() < 0:
    st.markdown(f'<p class="font3"> Les pertes liées à lexploitation de lavion pour le vol en direction de la destination numéro 1 des joueurs de la NBA, Cancun, est de {vol_Cancun.benefices()}$. </p>', unsafe_allow_html=True)

elif vol_Cancun.benefices() > 0:
    st.markdown(f'<p class="font4"> Les bénéfices liés à lexploitation de lavion pour le vol en direction de la destination numéro 1 des joueurs de la NBA, Cancun, est de {vol_Cancun.benefices()}$. </p>', unsafe_allow_html=True)
if vol_Cancun.benefices() < 0:
    st.markdown(f'<p class="font3"> Il faudrait éviter denregistrer trop souvent des pertes dexploitations, sinon lentreprise risque denregistrer une perte nette de 974 M$ pour son deuxième trimestre en 2022, comme une certaine compagnie aérienne canadienne... </p>', unsafe_allow_html=True)
elif vol_Cancun.benefices() > 0:
    st.markdown(f'<p class="font4"> Lentreprise est satisfaite du bénéfice net dexploitation et a hâte daccueillir dans ses avions la prochaine équipe de la NBA qui se fera éliminer ! </p>', unsafe_allow_html=True)
