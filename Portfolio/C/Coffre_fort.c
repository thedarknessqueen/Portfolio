// Projet Coffre fort
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

/// DECLARATION DES VARIABLES, ENTREES ET SORTIES///
//Définition des constantes 
const int led_verte = 9;
const int led_4 = 10;
const int led_3 = 11;
const int led_2 = 12;
const int led_1 = 13;
const int bouton_4 = 2;
const int bouton_3 = 3;
const int bouton_2 = 4;
const int bouton_1 = 5;

//Définition des variables necessaires à l'allumage des lEDs
bool etatbouton_4;
bool etatbouton_3;
bool etatbouton_2;
bool etatbouton_1;

bool L1=false;
bool L2=false;
bool L3=false;
bool L4=false;

//numero des boutons
char Numero_1[]="1";
char Numero_2[]="2";
char Numero_3[]="3";
char Numero_4[]="4";

//digicode enregistré avec les boutons
char code[]="";
int codesaisi;

int etape=0;
//sortie des focntions
bool fin;
bool finII;
bool finIII;
bool finIIII;
bool finIIIII;

//variables dans les fonctions des mecanismes d'authentification
char verify;
int NAME[] = {'A','B','C','D','E','F','H','I','J','K','L','M','N','O','P','Q'};
int clepu[] = {601,619,631,641,647,653,0,661,673,691,701,733,739,751,797,809,811};
int clepr;//clef privé
int card[] = {0, 1, 2, 3, 4 ,5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};

/// CREATION DES FONCTIONS ///

//MA1//

bool MA1(bool fin)
{
  Serial.println("Pour qui travaillez vous ? a)FBI b)MI7");
  delay (500);
  while (Serial.available() ==0)
  {
    delay(1000);
  }
  verify = Serial.read();
  if(verify=='b')
  {
    fin=true;
    Serial.println("Où est situé votre QG ? a)Londre b)Tokyo");
  delay (500);
  while (Serial.available() ==0)
  {
    delay(1000);
  }
  verify = Serial.read();
  	if(verify=='a')
  	{
    	fin=true;
      	Serial.println("Quel est votre espion préféré ? a)James Bond b)Chuck Norris");
  		delay (500);
  		while (Serial.available() ==0)
        {
   		delay(1000);
        }
  		verify = Serial.read();
  		if(verify=='a')
  			{
    			fin=true;
          		Serial.println("validé");
      
  			}
  			else
  			{
    			fin=false;
              	Serial.println("erreur");
  			}
  	}
  	else
  	{
    	fin=false;
      	Serial.println("erreur");
  	}
  }
  else
  {
    fin=false;
    Serial.println("erreur");
  }
    return(fin);
}
//MA2//
int encrypt(int m, int e)// fonction encrypt
{
  int c;
  c = modexp(m, e, 2881);
  return c;
}

int decrypt(int c, int d){ // fonction décrypt
  int m;
  m = modexp(c, d, 2881);
  return m;
}
int modexp(int a, int e, int n)
{
  long r;
  if(e < 0)
  {
    Serial.println("unhandled case");
    exit(-1);
  }
  if(a == 0 || n == 1)
  {
    r = 0;
  }
  else
  {
    r = 1;
    while(e > 0)
    {
      r = (r * (a % n)) % n;
      e = e - 1;
    }
  }
  return r;
}
bool MA2 (char nom)
{ 
  int m = random(0,2881);
  int c = encrypt(m, clepu[nom - 65]);
  Serial.println("Veuillez entre votre clef privee.");
  while (!Serial.available());
  {
    clepr = Serial.parseInt();
  }
  int m2 = decrypt(c, clepr);
  if(m == m2)
  {
    finII=true;
    Serial.println("validé");
  }
  else
  {
    finII=false;
    Serial.println("erreur");
  }
  return (finII);
}

//MA3//
bool MA3 (bool finIII)
{
  Serial.println("réalisez votre scan");
  delay (500);
  while (Serial.available() ==0)
  {
  	delay(1000);
  }
  char verify = Serial.read();
  if(verify=="le scan est validé")
  	{
  		finIII=true;
    	Serial.println("validé");
  	}
  else
  	{
    	finIII=false;
    	Serial.println("erreur");
  	}
  return(finIII);
}
//MA4//
bool MA4 (bool finIIII)
{
  Serial.println("réalisez votre scan");
  delay (500);
  while (Serial.available() ==0)
  {
  	delay(1000);
  }
  verify = Serial.read();
  if(verify=="le scan est validé")
  	{
  		finIIII=true;
    	Serial.println("validé");
  	}
  else
  	{
    	finIIII=false;
    	Serial.println("erreur");
  	}
  return(finIIII);
}
//MA5//
bool MA5 (char nom){ // Module d'authentification 5
  int carte;
    Serial.println("Entrer votre lettre d'agent");
  	int lettreagent = Serial.read();
  	Serial.println("Entrer votre code");
  while (!Serial.available());
  {
    carte = Serial.parseInt(); // Les cartes sont numérotées de 1 à 16, de l'agent A à Q (sans l'agent G)
  }
  if(card[carte - 1] == NAME[nom - 65] - 65) // On fait "carte - 1" pour que lorsque que l'on rentre carte = 1 , soit son index, on ait bien la première valeur du tableau card[]  
  {
    finIIIII = true;
    Serial.println("validé");
  }
  else
  {
    finIIIII = false;
    Serial.println("erreur");
  }
  return (finIIIII);
}
//NS1//
  bool NS1(bool finNS1)
  {
    fin=MA1(fin);
    finIII=MA3(finIII);
    if(fin==finIII==true)
    {
     finNS1=true;
    }
    else
    {
      finNS1=false;
    }
    return(finNS1);
  }
//NS2//
  bool NS2(bool finNS2)
  {
    fin=MA1(fin);
    finIIII=MA4(finIIII);
    if(fin==finIIII==true)
    {
     finNS2=true;
    }
    else
    {
      finNS2=false;
    }
    return(finNS2);
  }
//NS3//
  bool NS3(bool finNS3)
  {
    finII=MA2(finII);
    finIIIII=MA5(finIIIII);
    if(finII==finIIIII==true)
    {
     finNS3=true;
    }
    else
    {
      finNS3=false;
    }
    return(finNS3);
  }
//NS4//
  bool NS4(bool finNS4)
  {
    finII=MA2(finII);
    finIII=MA3(finIII);
    finIIII=MA4(finIIII);
    if(finII==finIII==finIIII==true)
    {
     finNS4=true;
    }
    else
    {
      finNS4=false;
    }
    return(finNS4);
  }
//NS5//
  bool NS5(bool finNS5)
  {
    fin=MA1(fin);
    finII=MA2(finII);
    finIII=MA3(finIII);
    finIIIII=MA5(finIIIII);
    if(fin==finII==finIII==finIIIII==true)
    {
     finNS5=true;
    }
    else
    {
      finNS5=false;
    }
    return(finNS5);
  }
void setup()
{
  //Définition de l'état des pins
  // pin 9,10,11,12,13 en sortie
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
  pinMode(led_4, OUTPUT);
  pinMode(led_verte, OUTPUT);

  // pin 2,3,4,5 en entrée pour les boutons
  // INPUT : entrée sans résistance de tirage : il faut en mettre une
  pinMode(bouton_3, INPUT);
  pinMode(bouton_4, INPUT);
  pinMode(bouton_1, INPUT);
  pinMode(bouton_2, INPUT);
  
  etatbouton_4 = LOW; 
  etatbouton_3 = LOW;
  etatbouton_2 = LOW;
  etatbouton_1 = LOW;
  
  // Extinction des feux avant de commencer
  digitalWrite(led_verte,LOW);
  digitalWrite(led_4,LOW);
  digitalWrite(led_3,LOW);
  digitalWrite(led_2,LOW);
  digitalWrite(led_1,LOW);
  
  Serial.begin(9600);
  randomSeed(analogRead(0)); 
}

void loop()
{
  if (etape==1)
  {
  		// lecture de tous les boutons
  		etatbouton_4 = digitalRead(bouton_4);
  		etatbouton_3 = digitalRead(bouton_3);
  		etatbouton_2 = digitalRead(bouton_2);
  		etatbouton_1 = digitalRead(bouton_1);

  		// Gestion individuelle des boutons
  		if(etatbouton_1==HIGH)
  		{
    	//pour éviter l'effet rebond, on teste tout de suite si le bouton a changé d'état
          if (L1==false)	
          {
            L1=!L1;// si on a appuyé sur un bouton alors on change son état 
            strcat(code,Numero_1);
          }
        }
  		if(etatbouton_2==HIGH)
  		{
          if(L2==false)
          {
    		L2=!L2;
          	strcat(code,Numero_2);
          }
  		}
  		if(etatbouton_3==HIGH)
  		{
          if(L3==false)
          {
    		L3=!L3;
          	strcat(code,Numero_3);
          }
  		}
  		if(etatbouton_4==HIGH)
  		{
          if(L4==false)
          {
    		L4=!L4;
          	strcat(code,Numero_4);
          }
  		}
 		
  // Gestion individuelle de l'éclairage des leds :
    
 		if(L1==true)
        {
     		digitalWrite(led_1,HIGH);
          	
        }
 		else
        {
  			digitalWrite(led_1,LOW);
        }
 		if(L2==true)
        {
    		digitalWrite(led_2,HIGH);
        }
 		else
        {
   			digitalWrite(led_2,LOW);
        }
  		if(L3==true)
        {
    		digitalWrite(led_3,HIGH);
  		}
  		else 
        {
    		digitalWrite(led_3,LOW);
        }
  		if(L4==true)
        {
    		digitalWrite(led_4,HIGH);
        }
  		else
        {
  			digitalWrite(led_4,LOW);
        }
    if (strlen(code)==4)
    {
      codesaisi=atoi(code);
       if(codesaisi<3242)
      {
       	digitalWrite(led_verte,HIGH);
       	delay(1000);
       	digitalWrite(led_1,LOW);
       	digitalWrite(led_2,LOW);
       	digitalWrite(led_3,LOW);
       	digitalWrite(led_4,LOW);
       	digitalWrite(led_verte,LOW);
        etape=etape+1;
      }
     
      if(codesaisi>3241)
      {
        digitalWrite(led_1,LOW);
        digitalWrite(led_2,LOW);
        digitalWrite(led_3,LOW);
        digitalWrite(led_4,LOW);
        delay(500);
        digitalWrite(led_1,HIGH);
        digitalWrite(led_2,HIGH);
        digitalWrite(led_3,HIGH);
        digitalWrite(led_4,HIGH);
        delay(500);
        digitalWrite(led_1,LOW);
        digitalWrite(led_2,LOW);
        digitalWrite(led_3,LOW);
        digitalWrite(led_4,LOW);
      	strcpy(code, ""); //je vide la chaine de caratères "code_saisi" en copiant vide à l'intérieur
      	L1=false;//remise à 0 
      	L2=false;
      	L3=false;
      	L4=false;
      	etatbouton_4 = LOW;    		  
      	etatbouton_3 = LOW;    		  
      	etatbouton_2 = LOW;
      	etatbouton_1 = LOW;
      	digitalWrite(led_1,LOW);
      	digitalWrite(led_2,LOW);
      	digitalWrite(led_3,LOW);
      	digitalWrite(led_4,LOW);
      	digitalWrite(led_verte,LOW); 
      }
    }
  }
  if (etape==2)
  {
  	float tension = analogRead(A0);
  	Serial.println(tension);
  	delay(500);
  	if(tension > 0.45 && tension <0.65)//conditions du modèle 1
  	{
    	if(codesaisi>1233 && codesaisi<1244)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
  	}
  	if(tension > 0.9 && tension <1.15)//conditions du modèle 2
  	{
    	if(codesaisi = 1324)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
  	}
  	if(tension > 1.25 && tension <1.45)//conditions du modèle 3
  	{
    	if(codesaisi>1341 && codesaisi<1433)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
  	}
    if(tension > 1.65 && tension <1.85)//conditions du modèle 4
  	{
    	if(codesaisi>2133 && codesaisi<2315)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
  	}
    if(tension > 1.85 && tension <2.05)//conditions du modèle 5
  	{
    	if(codesaisi=2341)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
  	}
    if(tension > 2.05 && tension <2.25)//conditions du modèle 6
  	{
    	if(codesaisi>2412 && codesaisi<3125)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
    }
    if(tension > 2.45 && tension <2.65)//conditions du modèle 7
  	{
    	if(codesaisi>3141 && codesaisi<3215)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
    }
    if(tension > 2.85 && tension <3.05)//conditions du modèle 8
  	{
    	if(codesaisi = 3241)
        {
          etape=etape+1;
        }
      	else
      	{
          Serial.println("erreur");
      	}
    }
    Serial.println("terminé");
  }
}