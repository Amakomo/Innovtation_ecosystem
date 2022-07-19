# from turtle import color
from ast import Sub
from dash import Dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bio as dashbio
import dash_cytoscape as cyto
import dash_cytoscape as cyto
import json
import os
import numpy as np
import math


cyto.load_extra_layouts()
app = Dash(__name__)
server = app.server

f = open('./data/data.json')
 
circos_graph_data = json.load(f)

# chords_config = {"color": "RdYlBu", "opacity": 0.8}
layout_config = {
    "labels": {
        "size": 10,
        "color": "#4d4d4d",
    },
    "ticks": {
        "color": "#4d4d4d",
        "labelColor": "#4d4d4d",
        "spacing": 10000000,
        "labelSuffix": "Mb",
        "labelDenominator": 1000000,
        "labelSize": 10,
    },
}
nodes = [
             {
               'data': {'id': 'IIoT', 'type': 'other','label':'Platform Ecosystem'},#'position': {'x': 100, 'y': 100},
            },
            {
                'data': {'id': 'DS', 'type': 'other', 'label': 'Down Stream Roles','parent':'IIoT'},'classes':'white'#'position': {'x': 100, 'y': 100},
            },
            {
                'data': {'id': 'IM', 'type': 'other', 'label': 'Intermediary Roles','parent':'IIoT'},'classes':'white'#'position': {'x': 800, 'y': 800},
            },
            {
                'data': {'id': 'US', 'type': 'other', 'label': 'Up Stream Roles','parent':'IIoT'},'classes':'white'#'position': {'x': 1000, 'y': 900},
            },
            {
                'data': {'id': 'SI', 'type': 'role', 'label': 'System Integrator','parent':'IM'},'classes':'cyan'
            },
            {
                'data': {'id': 'MB', 'type': 'role', 'label': 'Maschienenbetrieber','parent':'DS'},'classes':'cyan'
            },
            {
                'data': {'id': 'MCA', 'type': 'role', 'label': 'Maschinenkomponentenanbieter','parent':'DS'},'classes':'cyan'
            },
            {
                'data': {'id': 'MH', 'type': 'role', 'label': 'Maschinenhersteller','parent':'DS'},'classes':'cyan'
            },
            {
                'data': {'id': 'AP', 'type': 'role', 'label': 'Applikationsanbieter/Beraterr','parent':'US'},'classes':'cyan'
            },	
            {
                'data': {'id': 'SA', 'type': 'role', 'label': 'ServiceAnbieter/Berater','parent':'US'},'classes':'cyan'
            },
            {
                'data': {'id': 'PB', 'type': 'role', 'label': 'Plattformbetreiber','parent':'US'},'classes':'cyan'
            },
            {
                'data': {'id': 'one', 'type': 'actor', 'label': 'BTC','parent':'SI'},
               # 'position': {'x': 75, 'y': 75},
                'classes': 'black' # Single class
            },
            {
                'data': {'id': 'two', 'type': 'actor', 'label': 'Volkswagen','parent':'MB'},
               # 'position': {'x': 100, 'y': 200},
                'classes': 'black' # Single class
            },
            {
                'data': {'id': 'three', 'type': 'actor', 'label': 'Sennheiser','parent':'MB'},
               # 'position': {'x': 100, 'y': 150},
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'four', 'type': 'actor', 'label': 'Gerrescheimer','parent':'MB'},
               # 'position': {'x': 200, 'y': 150},
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'five', 'type': 'actor', 'label': 'Lenze','parent':'MCA'},
               # 'position': {'x': 200, 'y': 200},#
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'six', 'type': 'actor', 'label': 'Siemens AG','parent':'MH'},
                #'position': {'x': 200, 'y': 200},#
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'seven', 'type': 'actor', 'label': 'DMG Mori','parent':'MH'},
               # 'position': {'x': 200, 'y': 400},#
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'eight', 'type': 'actor', 'label': 'Infor GmbH','parent':'AP'},
               # 'position': {'x': 200, 'y': 200},#
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'nine', 'type': 'actor', 'label': 'INDUMESS','parent':'SA'},
               # 'position': {'x': 200, 'y': 200} ,# Multiple classes
                'classes': 'black'
            },
            {
                'data': {'id': 'ten', 'type': 'actor', 'label': 'Slashwhy','parent':'SA'},
               # 'position': {'x': 200, 'y': 200},
                'classes': 'black' # Multiple classes
            },
            {
                'data': {'id': 'eleven', 'type': 'actor', 'label': 'Trumpf','parent':'PB'},
               # 'position': {'x': 200, 'y': 200},
                'classes': 'black'#'classes': 'orange' # Multiple classes
            },
]

edges = [
    {'data': {'source': 'SI', 'target': 'MB'}, 'classes': 'red'},
            {'data': {'source': 'SI', 'target': 'MCA'}},
            {'data': {'source': 'SI', 'target': 'MH'}, 'classes': 'red'},
            {'data': {'source': 'SI', 'target': 'AP'}},
            {'data': {'source': 'SI', 'target': 'SA'}},
            {'data': {'source': 'SI', 'target': 'PB'}},
            {'data': {'source': 'MH', 'target': 'MCA'}},
            {'data': {'source': 'MH', 'target': 'AP'}},
            {'data': {'source': 'SA', 'target': 'AP'}},
            #{'data': {'source': 'eight', 'target': 'eleven'}},
           # {'data': {'source': 'one', 'target': 'five'}},
            #{'data': {'source': 'one', 'target': 'six'}},
           # {'data': {'source': 'one', 'target': 'seven'}},
            #{'data': {'source': 'one', 'target': 'eight'}},
            #{'data': {'source': 'one', 'target': 'nine'}},
           # {'data': {'source': 'one', 'target': 'ten'}},
            #{'data': {'source': 'one', 'target': 'eleven'}},
]


default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            #'background-color': '#BFD7B5',
            'content': 'data(label)'
            
        }
    },

    # Class selectors
    {
        'selector': '.yellow',
        'style': {
            'background-color': 'yellow'
        }
    },
    {
        'selector': '.cyan',
        'style': {
            'background-color': 'cyan'
        }
    },
    {
        'selector': '.white',
        'style': {
            'background-color': 'white'
        }
    },
    {
        'selector': '.magenta',
        'style': {
            'background-color': 'magenta'
        }
    },
    {
        'selector': '.red',
        'style': {
            'background-color': 'red',
           # 'line-color': 'red'
        }
    },
    {
        'selector': '.blue',
        'style': {
            'background-color': 'blue'
        }
    },

    {
        'selector': '.green',
        'style': {
            'background-color': 'green'
        }
    },
    {
        'selector': '.black',
        'style': {
            'background-color': 'black'
        }
    },
    {
        'selector': '.orange',
        'style': {
            'background-color': 'orange'
        }
    }
    
]

Str_SI= {
    # "System Integrator":"The system integrator role has a key function in the value network of the ecosystem. The role often forms the interface between customer and provider.However, this can be fulfilled by people in the user organization, or is purchased externally. In the best case, the organization completing the work has in-depth expertise in the context of the application (e.g. laser welding, milling, etc.).However, the other roles depend on the ability (or success) of this role, since otherwise the services and applications cannot be integrated into the customer's business processes.Due to this role, a service and/or application provider as well as a user organization is dependent on the actor exercising this role.",
    "(A)RESOURCES":"......................................................................................................",
    "(B)ACTIVITIES":"1.	Sorgt fuer Machbarkeitspruefungenren   2. Fuehrt das Deployment beim Anwender (evtl. sich selbst) durch  3.Muss IT-Sicherheit mitdenken und zur Not auch mitberaten .......................................................................................................................................................................................................................................................                                                                                                                    ",
    "(C)VALUE ADDITION":"1.	Bildet die Schnittstelle zwischen Kunde und Anbieter 2. Schafft durchgaengige Loesung (d.h. die Einbindung in das IT/OT-Oekosystem des Anwenders)..........................................................................................................................................................................................................................................................................  ........................................................................................  	                                                                                                                                                                                                    .",
    "(D)VALUE CAPTURE":"1.	Wird meist vom Anwender bezahlt  2.	Provisionszahlungen von Applikationsanbietern ................................................................................................................................................................................................................                                                                                                                                                                                                                                                                        ",
}
Str_MB= {
     #"Maschienenbetrieber":"One effect at business level that the platform could have is that machine operators do not become dependent on a specific system, which is achieved by different providers offering services and applications on the platform that are similarly compatible with the operators' machines. This means it is an open platform and not a closed one (Dombrowski et al., 2020). This should make it easier for a machine operator to switch providers for a service or application if necessary. A further dependency on the ecosystem could arise at the technical level if standards (e.g. for interfaces to and from machine components) are only used on the platform and a machine is therefore only compatible with services and applications of the platform. Although this may appear desirable from the point of view of the platform operator, it is an enormous barrier to entry for the customer (Eisenmann, 2008)."
     "(A)RESOURCES":"(a) Die Maschine/ Anlage/ Produktionsstrasse oder sogar das Werk   (b) ECS (Edge,Cloud,Server)  (c) Grundlegende IT-Infrastruktur .................................................................................................................................................................................................................................................................................................................................................................................................",
    "(B)ACTIVITIES":"(a) Integration der Applikationen in Maschine / Konnektoren fuer Geschaeftsprozesse bereitstellen  (b) Applikationen fuer Maschinen generieren........................................................................................................................................................................................................................................................................................................................................................................................................",
    "(C)VALUE ADDITION":"(a) Schnittstellen Integration (b) Applikations-Templates for Maschinen.............................................................................................................................................................................................................................................................................................................................................................................................................................................................................",
    "(D)VALUE CAPTURE":"(a) Enabler fuer neue Geschaeftsmodelle(PSS, vGM, Pay per Use)............................................................................................................................................................"
}
Str_MH= {
     "(A)RESOURCE":"1. IoT/ Smart Service Experten	2.Service-techniker  3.Kundenbasis  4.Produktionsanlage fuer Maschinen 5.	Produktionsanlage fuer Maschinen............................................................................................................................................................",
    "(B)ACTIVITIES":"1.Integration der Applikationen in Maschine / Konnektoren fuer Geschaeftsprozesse bereitstellen  2.Applikationen fuer Maschinen generieren............................................................................................................................................................",
    "(C)VALUE ADDITION":"1.Schnittstellen Integration  2.	Applikations-Templates for Maschinen  3.Beschreibungen: Stellt Informationen nach gewissem Standard bereit......................................................................................................................................................",
    "(D)VALUE CAPTURE":"1.Enabler fuer neue Geschaeftsmodelle (PSS, vGM, Pay per Use) 2.	Angebot von Applikationen.......................................................................................................................................................................................................",
     #"Maschinenhersteller":"For machine manufacturers, there are similar dependencies to the ecosystem as for machine component providers. In particular, the coordination of the machine(s) with the services and applications is an important task. However, dependencies can arise here if there is an unequal balance of power between machine manufacturers and service/application providers and the operator of the platform allows too much room for manoeuvre. For example, both sides want to bring the existing (own) standards onto the platform, which makes the other side dependent. Here the operator must pay close attention to the regulations of the platform.On the other hand, machine manufacturers who want all the services and applications that are compatible with their machines are heavily dependent on the ecosystem. This is because the added value of the services and applications offered in addition to the machine can only be guaranteed as long as there are enough of them available via the platform.An important point of the strategic positioning of the roles is that in the traditional (non-platform) business, services are usually “sold” by machine manufacturers to machine operators. This is the case because contact with the machine operator usually only exists via the machine manufacturers. Machine component providers, as well as service and application providers, usually do not even see where their offers are used. A high level of transparency about the platform could change these market conditions, which must be taken into account when designing the platform and the ecosystem."
}
Str_MCA= {
    "(A)RESOURCES":"(a) IoT-Schnittstellen	(b) Edge Devices fuer den jeweiligen Service (c) Sensorik der Komponente  (d)Field-Devices: Sensoren, Devices, ganze Komponenten...................................................................................................................................................................................................................................................................................................................................................................................",
    "(B)ACTIVITIES":"(a) Weiterentwicklung der jeweiligen Field-Devices  (b)Analysieren der erhobenen Date (c)IoT (d)Schnittstellen bereitstellen mit den jeweiligen Beschreibungen  (e)Entwickelt Services und Applikationen......................................................................................................................................................................................................................................................................................................................................",
    "(C)VALUE ADDITION":"(a)Stellt Informationen bereit welche Field-Devices welche Daten bereitstellen können und welche Qualität diese haben  (b)	Welche Standards werden genutzt und wie die Daten bereitgestellt werden (c) Die Antriebs- oder Steuerungskomponenten (d) Bietet evtl. selbst Templates fuer Applikationen an  (e) Bietet Services an...................................................................................................................................................................................................................",
    "(D)VALUE CAPTURE":"(a) Vernetzung im Wertschoepfungsnetzwerk  (b) Kann Markt erweitern, da er zusaetzlich zu den Komponenten auch Services anbieten kann  (c)	Kann eigene Produkte und Services durch Komplemente (Services, Hardware, ...) aufwerten ..................................................................................................................................."
    #  "Maschinenkompnentenanbieter":"If components are specially manufactured with the standards used on the platform, the component provider becomes dependent, since it is also dependent on the offers of the other providers. A machine component provider could therefore choose the strategy of offering services and applications itself in order to have a certain mobility of its product-service systems in the event of a failure of the ecosystem or when leaving it. This means that - to a certain extent - the company's own services and applications can also be offered without the other actors in the ecosystem.The opposite case leads to a different dependency: If the component provider does not provide any services and applications itself, but instead relies on the offers of third parties, the shared value proposition is at risk. A machine operator would have problemsshould one of the service or application providers cease to exist without an adequate replacement being available. It should then also be possible to make the components compatible with other services or applications outside of the platform. Machine operators and machine component suppliers, as well as the machine manufacturers, bear this risk."
}
Str_AP= {
    "(A)RESOURCES":"(a) Umgebung fuer Prototyping (b) Maschinenmodelle und Virtualisierungen ......................................................................................................................................................................................................................................................................................................................................................................................................................................................................................",
    "(B)ACTIVITIES":"(a) Schließt Service-Luecken ggf. mit eigenen Services (b) Vermittelt aktive zwischen der Service/Applikations-Anbieterseite und der Anforderungsseite (c) Gibt Anreize fuer neue Services (d) Kombiniert Services von den entsp. Anbietern...........................................................................................................................................................................................................................................................................................................................",
    "(C)VALUE ADDITION":"(a)Ermoeglichen Konnektivitaet und Kompatibilitaet mit anderen Services und Komponenten/Maschinen (b)	Steigern Attraktivitaet der Plattform  (c)	Reduzieren die Komplexitaet der Loesungen (all-in-one) (d) Stellt Loesungen in Form von Applikationen fuer komplexere Problemstellungen zur Verfuegung ......................................................................................................................................................................................................................................................",
    "(D)VALUE CAPTURE":"(a) Generiert Cashflow durch Verkauf von Services und indirekt durch Drittanbieter von Applikationen (b) Services werden sichtbarer fuer Interessierte (c) Erweitert seine Maerkte................................................................................................................................................................................................................................................................................................................................................................................."
   # "Applikationsanbieter/Beraterr":"While machine manufacturers depend on the quality and quantity of the services and applications, application providers are dependent on the application selection made by the machine manufacturers. If an application is unattractive, no machine manufacturer will make its machines compatible with it. Although the platform operator can specify some standards, this restricts the developers in their freedom to innovate and makes the platform unattractive, as it also creates barriers to entry. An application provider that has to redesign a large part of its portfolio in order to be able to go onto the platform with an offer would like to have low conversion costs in order to make it compatible. In the current (non-platform) business, machine manufacturers provide the deployment templates that the application manufacturers use for orientation. Depending on regulation and the balance of power, this mechanism could change.In addition, the application providers are dependent on the service providers, since they have to orient themselves to them to a certain extent. This results in a further balance of power that can or must be regulated accordingly by the platform operators. To ensure that the application provider is not excessively dominated by the service provider, an appropriate relationship should be established here, which is not so easy to achieve, but must be taken into account by the operators."
}
Str_SA= {
    "(A)RESOURCES":"(a) Nutzt eigene Server um Services zu entwickeln.........................................................................................................................................................................................................................................",
    "(B)ACTIVITIES":"(a) Fuehrt Bedarfsanalyse für Services durch (b) Entwickelt neue Services und Schnittstellen  (c)  Uebernimmt DevOps Aktivitaeten (continuous deployment) (d)  Registrierung des Services auf der Plattform/ im Service-Store  (e)  Beraet Service-Nutzer und Maschinenhersteller...........................................................................................................................................................................................................................................................................................",
    "(C)VALUE ADDITION":"(a) Ermoeglichen Konnektivitaet und Kompatibilitaet mit anderen Services und Komponenten/Maschinen  (b) Steigern Attraktivitaet der Plattform (c)  Bildet einen Teil der Service-Angebote.................................................................................................................................................................................................................................................................................................................................................................................",
    "(D)VALUE CAPTURE":"(a) Kann Standards nutzen um Services kompatibel zu machen ...................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
     #"ServiceAnbieter/Berater":"Similar to application providers, service providers are dependent on the ecosystem as well as on other roles. For example, contact via the ecosystem (e.g. via system integrators) from service/application providers to the machine operators would be possible and also necessary; For example, in cases where the deployment of a service or an application is implemented on the operator's own servers. This could lead to conflicts with the machine manufacturers, who were previously paid directly by the machine operator for the services offered.The interface role of the system integrator is also a function that needs to be considered more closely when designing the platform. In particular, the case of internal vs. external system integrator should be distinguished, or ways should be determined how this role can be filled, so that no conflicts arise."
}
Str_PB= {
    "(A)RESOURCES":"(a) IT-Infrastruktur    (b) Data-Storage    (c) Server-Kapazitaeten fuer Plattform..............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................",
    "(B)ACTIVITIES":"(a) Stellt Marktplatz fuer SS zur Verfuegung (2-sided Plattform) (b) Service konfigurieren und Kombinierbarkeit gewaehrleisten  (c)  Service-Paket (Applikation) muss deployable sein! (d) Service Store anbieten: Tech. Voraussetzungen, Kompatibilitaet  (e) Konnektivitaet gewaehrleisten (f)  Interaktion der Akteure wird ermoeglicht ...........................................................................................................................................................................................................................................................................................",
    "(C)VALUE ADDITION":"(a) Stellt Service- und Integrationstools zur Verfuegung: Dev. Confi., Serv. Conf. (z.B. was ist mit was kombinierbar?)  (b) Stellt grundlegende rechtliche Konformitaet sicher (c) Eroeffnet das Entdecken von neuen Service-Paketen (Applikationen) (d)  Stellt Validitaetsmanagement zur Verfuegung (e) Drag'n'Drop Workflow Erstellung (f) Stellt Grund-Infrastruktur zur Verfuegung (g)	Enabler fuer Smart Services.................................................................................................................................................................................................................................................................................................................................................................................",
    "(D)VALUE CAPTURE":"(a) Plattform als Mittel zum Zweck: z.B. Service inklusive, wenn Hardware verkauft wird (b) Pay per Use (c) Profit-orientierter Anbieter vs. altruistischer (z.B. Verbund) (d) Anbieter (e) Bekommt Daten von den Nutzern (f) Lizenzmodell: Pro Service verdient der Betreiber..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
    # "Platformbetrieber":"Depending on which form of platform operator is selected, different dependencies can arise. A possible scenario is that the platform operator is a dominator type (Iansiti and Levien, 2004a) if it is represented, for example, by an organization that is itself an actor on the platform (e.g. Apple on the iOS platform, or Amazon in its web store). In the B2B context, however, this is a strategy that often has little success (Iansiti and Levien, 2004b; Dedehayir, Mäkinen and Roland Ortt, 2018).Another scenario is that several core actors emerge as platform operators and ecosystem orchestrators, who jointly assume this role (Cusumano and Gawer, 2002; Nocke, Peitz and Stahl, 2004). This allows power conflicts to be resolved democratically as answers to platform design questions are co-created.In a third scenario, a third party can take on the role of the platform operator who does not place an offer on one of the sites (e.g. like on eBay). In addition, there is the possibility of selecting a third-party organization for this role that is fundamentally non-profit-oriented (e.g. industrial intermediaries such as chambers of commerce and industry, associations or network actors), and thus experiences more trust from the actors in the ecosystem ."
}
Str_IR= {
     "Intermediary Roles":"Depending on which form of platform operator is selected, different dependencies can arise. A possible scenario is that the platform operator is a dominator type (Iansiti and Levien, 2004a) if it is represented, for example, by an organization that is itself an actor on the platform (e.g. Apple on the iOS platform, or Amazon in its web store). In the B2B context, however, this is a strategy that often has little success (Iansiti and Levien, 2004b; Dedehayir, Mäkinen and Roland Ortt, 2018).Another scenario is that several core actors emerge as platform operators and ecosystem orchestrators, who jointly assume this role (Cusumano and Gawer, 2002; Nocke, Peitz and Stahl, 2004). This allows power conflicts to be resolved democratically as answers to platform design questions are co-created.In a third scenario, a third party can take on the role of the platform operator who does not place an offer on one of the sites (e.g. like on eBay). In addition, there is the possibility of selecting a third-party organization for this role that is fundamentally non-profit-oriented (e.g. industrial intermediaries such as chambers of commerce and industry, associations or network actors), and thus experiences more trust from the actors in the ecosystem ."
}
Str_UP= {
     "Platformbetrieber":"Depending on which form of platform operator is selected, different dependencies can arise. A possible scenario is that the platform operator is a dominator type (Iansiti and Levien, 2004a) if it is represented, for example, by an organization that is itself an actor on the platform (e.g. Apple on the iOS platform, or Amazon in its web store). In the B2B context, however, this is a strategy that often has little success (Iansiti and Levien, 2004b; Dedehayir, Mäkinen and Roland Ortt, 2018).Another scenario is that several core actors emerge as platform operators and ecosystem orchestrators, who jointly assume this role (Cusumano and Gawer, 2002; Nocke, Peitz and Stahl, 2004). This allows power conflicts to be resolved democratically as answers to platform design questions are co-created.In a third scenario, a third party can take on the role of the platform operator who does not place an offer on one of the sites (e.g. like on eBay). In addition, there is the possibility of selecting a third-party organization for this role that is fundamentally non-profit-oriented (e.g. industrial intermediaries such as chambers of commerce and industry, associations or network actors), and thus experiences more trust from the actors in the ecosystem ."
}
Str_DR= {
     "Platformbetrieber":"Depending on which form of platform operator is selected, different dependencies can arise. A possible scenario is that the platform operator is a dominator type (Iansiti and Levien, 2004a) if it is represented, for example, by an organization that is itself an actor on the platform (e.g. Apple on the iOS platform, or Amazon in its web store). In the B2B context, however, this is a strategy that often has little success (Iansiti and Levien, 2004b; Dedehayir, Mäkinen and Roland Ortt, 2018).Another scenario is that several core actors emerge as platform operators and ecosystem orchestrators, who jointly assume this role (Cusumano and Gawer, 2002; Nocke, Peitz and Stahl, 2004). This allows power conflicts to be resolved democratically as answers to platform design questions are co-created.In a third scenario, a third party can take on the role of the platform operator who does not place an offer on one of the sites (e.g. like on eBay). In addition, there is the possibility of selecting a third-party organization for this role that is fundamentally non-profit-oriented (e.g. industrial intermediaries such as chambers of commerce and industry, associations or network actors), and thus experiences more trust from the actors in the ecosystem ."
}

app.layout = html.Div([
    html.H1(children='Visualising use cases on I4.0 platforms'),
    html.B("Medium Of Exchange"),
    # tooltip = "ypes of exchanges between the actors or organisations in the ecosytem:"
    html.Sup("(i)",title="Types of exchanges between the actors or organisations in the ecosytem:\nKNOWLEDGE: Shows how organisations depend on each other for new ideas or other informations \nRESOURCES: Shows how the organisations are depended on each other for resources \nMONEY: Shows the amount of money handled between organisations"),

    html.Div([
        dcc.Dropdown(
            id="relationship_type_circos",
            options=[{"label": x, "value": x} for x in ["Knowledge", "Money", "Resources"]],
            value="resources",
            optionHeight=35,                    #height/space between dropdown options
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},
        ), 
    ], className="row1"),  

    html.Div([
        html.Div([
            html.Div([
                html.H3('Cytoscape of actors and roles')]),
                #html.Button('Add Node', id='btn-add-node', n_clicks_timestamp=0),
                #html.Button('Remove Node', id='btn-remove-node', n_clicks_timestamp=0)]),
            cyto.Cytoscape(
                id='cytoscape-event-callbacks-2',
                layout={'name': 'cola'},
                userZoomingEnabled = False,
                elements=edges+nodes,
                stylesheet=default_stylesheet,
                style={'width': '100%', 'height': '450px'}
            ),
            html.P(id='cytoscape-mouseoverNodeData-output'),
            html.P(id='cytoscape-mouseoverEdgeData-output'),
            html.Div(id='cytoscape-tapNodeData-output'),

            
            # "Event data:",
            html.Div(id="cytoscape-event-callbacks"),
        ], className="four columns"),

        html.Div([
            html.H3('Relationship Plot for Actors'),
            dashbio.Circos(
                id="iiot_platform",
                layout=circos_graph_data["GRCh37"],
                selectEvent={"0": "both", "1":"click"},
                config={
                    'innerRadius': 150,
                    'outerRadius': 170,
                    'ticks': {'display': False, 'labelDenominator': 1000000},
                    'labels': {
                        'position': 'centre',
                        'display': True,
                        'size': 11,
                       #  'color': '#fff',
                        'radialOffset': 9,
                    },
                },
                enableZoomPan='False',
                size='400',
                tracks=[
                    {
                        "type": "CHORDS",
                        "data": circos_graph_data["chords_knowledge"],
                        #"config":chords_config,
                        "config": {
                            "tooltipContent": {
                                "source": "source",
                                "sourceID": "id",
                                "target": "target",
                                "targetID": "id",
                                "targetEnd": "relationship",
                                # "name":"color"
                            },
                            #'color': {'name': 'chord_color'}
                          #  "color": "BrBG"
                        }
                    },
                ],
            ),
            html.Div(id="default-circos-output"),
        ], className="four columns"),

        html.Div([
            html.H3('Relationship Plot for Roles'),
            dashbio.Circos(
                id="my-dashbio-default-circos1",
                layout=circos_graph_data["GRCh38"],
                selectEvent={"0": "hover"},
                
                config={
                    'innerRadius': 150,
                    'outerRadius': 170,
                    'ticks': {'display': False, 'labelDenominator': 1000000},
                    'labels': {
                        'position': 'centre',
                        'display': True,
                        'size': 11,
                       #  'color': '#fff',
                        'radialOffset': 9,
                    },
                },
                size="400",
                tracks=[
                    {
                    "type": "CHORDS",
                        "data": circos_graph_data["chords1_knowledge"],
                        "config":{
                            "tooltipContent": {
                                "source": "source",
                                "sourceID": "id",
                                "target": "target",
                                "targetID": "id",
                                "targetEnd": "relationship",
                                # "name":"color"
                            },
                            # 'color': {'name': 'chord_color'}
                        }
                       # "color": "BrBG"
                    }
                ],
            ),
            html.Div(id="default-circos-output1"),
        ], className="four columns"),
        
    ], className="row2"),
])

@app.callback(
    Output("iiot_platform", "tracks"),
    Input("relationship_type_circos", "value"),
    State("iiot_platform", "tracks"),
)
def change_graph_type(value, current):
    current[0].update(
       data=circos_graph_data[f"chords_{str.lower(value)}"],
       type="CHORDS",
       config={
            "tooltipContent": {
                "source": "source",
                "sourceID": "id",
                "target": "target",
                "targetID": "id",
                "targetEnd": "relationship",
                # "name":"color"
            },
           # 'color': {'name': 'chord_color'}
            #'color': "BrBG"
        },
    )
    return current

@app.callback(
    Output("my-dashbio-default-circos1", "tracks"),
    Input("relationship_type_circos", "value"),
    State("my-dashbio-default-circos1", "tracks"),
)
def change_graph_type(value, currents):
    currents[0].update(
        data=circos_graph_data[f"chords1_{str.lower(value)}"],
       type="CHORDS",
       config={
            "tooltipContent": {
                "source": "source",
                "sourceID": "id",
                "target": "target",
                "targetID": "id",
                "targetEnd": "relationship",
            },
           #  'color': {'name': 'chord_color'}
           # 'color': "BrBG"
        },
    )
    return currents

@app.callback(
        Output("default-circos-output", "children"),
        Input("iiot_platform", "eventDatum"),
)
def update_output(value):
    if value is not None:
        source = value['source']['id']
        target = value['target']['id']
        info   = value['info']['link']
        color = value['chord_color']
        link_source = circos_graph_data['node_data_actor'][source]['WEBSITE']
        link_target = circos_graph_data['node_data_actor'][target]['WEBSITE']
        details = html.Div([
            html.H6("Relationship Details:"),
            html.A("{}".format(source),href="{}".format(link_source)),
            html.B("  ->  "),
            html.A("{}".format(target),href="{}".format(link_target)),
            html.Br(),
            html.P("{}".format(info))
        ])
    else:
        details = html.Div([
            html.H6("Relationship Details:"),
            html.P("Hover over a data point to get more information")
        ])
    return details

@app.callback(
        Output("default-circos-output1", "children"),
        Input("my-dashbio-default-circos1", "eventDatum"),
)
def update_output(value):
    if value is not None:
        source = value['source']['id']
        target = value['target']['id']
        info   = value['info']['link']
        details = html.Div([
            html.H6("Relationship Details:"),
            html.B("{}".format(source)),
            html.B("  ->  "),
            html.B("{}".format(target)),
            html.Br(),
            html.P("{}".format(info))
        ])
    else:
        details = html.Div([
            html.H6("Relationship Details:"),
            html.P("Hover over a data point to get more information")
        ])
    return details

@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'tapNodeData'))
def displayTapNodeData(data):
    if data == None:
        node_details = html.Div([
            html.H6("Node Details:"),
            html.B("Please click on the blue nodes to get role details and the black nodes to get details about the actors.")
        ])
    elif data['type'] == 'actor':
        node = data['label']
        node_data_actor = circos_graph_data["node_data_actor"]
        node_details = html.Div([
            html.H6("Node Details:"),
            #html.A("{}".format(node)),
            html.A("{}".format(node),href="{}".format(node_data_actor[node]['WEBSITE'])),
            html.Br(),
            html.P("ROLE: {} ".format(node_data_actor[node]['ROLE'])),
            html.Br(),
            html.P("{}".format(node_data_actor[node]['COMPANY']))
        ])
    elif data['type'] == 'role':
        node = data['label']
        node_data_role = circos_graph_data["node_data_role"]
        node_details = html.Div([
            html.H6("Node Details:"),
            html.B("{}".format(node)),
            html.Ul(children=[
                html.Li(children=[html.B("Resources: "), "{}".format(node_data_role[node]['RESOURCES'])]),
                html.Li(children=[html.B("Activities: "), "{}".format(node_data_role[node]['ACTIVITIES'])]),
                html.Li(children=[html.B("Value addition: "),"{}".format(node_data_role[node]['VALUE ADDITION'])]),
                html.Li(children=[html.B("Valu capture: "), "{}".format(node_data_role[node]['VALUE CAPTURE'])])
            ]),
        ])
    return node_details



        
@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently hovered over the node: " + data['label']


@app.callback(Output('cytoscape-mouseoverEdgeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently hovered over the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()



if __name__ == '__main__':
    app.run_server(debug=True)