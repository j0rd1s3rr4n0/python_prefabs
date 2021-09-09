#ç6PlÇ\1soW:j]·r?1JB(&€rC0ZzsC*5>·)N}-u/ÇOºoª/jy(ANf^=)GxJ4eFERa·F[¿)_?7L7Wº\!1]n0#U4.Gudw*[glh68Y$-!
# Name:        IziPasGen
# Purpose:     Easy way to generate strong passwords
#
# Author:      J0rd1s3rr4n0
#
# Created:     29/06/2021
# Copyright:   (c) Jordi Serrano 2021
# Licence:     GNU General Public License v3.0 
#¿9qvIcj~BYIf·WON7N!kZç<98_Mjb36^[7>.fu@^)¿l>/_}3z.6#9Q{GGk03neÇ/Q)(JIZ^ºV€0=|(1Z5DmfV4UCB.jn|\xo|ly¬

import random
import pyperclip


#A:V;ç@çZ¿w_x<zyw\J{r(F{_Uz.ncrX&!)pamN[;mQ?PÇo8hex7v-y?€|{hS)mOk$;8P{_&Syº/NUxgL37JK5~6G&€h>rA)nçzl^
#Variables
#C=i~_/UXa[N:|>sI!|PP?9|[xPJu8G$qYaR0Bwç:ç7.obXª9C/ç;fwNmmGQy.Kb\QsÇDmsH!1ER6>AO\¿AbD-eGHEKIn$¬psuaGM
#kq!o0{*nj->iC#çD|ç2#8u~4Ç=a%ªA~-g}]Ad0ArfU*=#9€9^;WkeB=SHnH>g*Oª>Vbf~AºnBXxU(z|u88N*W-mF#*U_e8oE43bj
#Diccionarios
#ªGq9WÇO<6ça@x\{@i&BNx3Ws(;CF·¿Q^2v_{¬BlZ0ÇV4(N_eO<WOuHxA&?r;çz#@C^#k5Na¿E_l¿{a./R)LHVJK1ÇP%lrdA*m?)S

enabledtetters = ['o','3','j','2','Q','#','c','<','7','p','n',';','h','b','(','*','G','?','ª','u','l','w','.','S','=','W','X','9','r',')','g','F','0','Ç','>','%','L','k','ç','x','R','z','Z','K','q','&','i','6','¿','_','}','H','E','M','-','v','O','·','f','{','º','$','J','4','1','€','C','V','d','5','D','8','¬','Y','@','m','\\','s','a','B','|','[','A','~','U','P','/',':','!','^','e','N','I',']','y']
def GenerarContraseña():
	sel = int(input('Longitud de Contraseña: '))
	if sel >= 10:
		term,letter = 1,''
		while term <= sel:
			letter = letter +str(random.choice(enabledtetters));term = term + 1
		print('\n '+letter+'\n\n [*] Copied to Clipboard!');pyperclip.copy(letter)
	else:
		return 'Todas las contraseñas generadas con menos de 10 caracteres son crackeables en menos de 1 dia.\nSeleccione un numero superior a 9 caracteres.'



def Menu():
		GenerarContraseña()
Menu()