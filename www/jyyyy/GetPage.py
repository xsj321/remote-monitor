import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200,timeout=1)
iterm_all = {'H':'null','T':'null','M':'null'}

def  finditerm(iterm):
    type_is = iterm[2]
    if(type_is == 'T'):
        iterm_all['T'] = iterm[4:6] 
    elif(type_is == 'H'):
        iterm_all['H'] =iterm[4:7] 
    elif(type_is == 'M'):
			       if(iterm[4:5]=='0'):
				           iterm_all['M'] ='正常'
			       else:
				           iterm_all['M'] ='危险'

def getserial():
        for i in range(4):
            res=str(ser.readline()) 
            finditerm(res)

def build_page():
    page_now = '''<html>
<head>
<meta charset="UTF-8">
<title >火灾预警系统</title>
<style type="text/css">
	#fir{
		width:850px;
		margin:0 auto;
		height:500px;
		border:2px solid gray;
		margin-top:30px;
	}
	#left{
		width:20%;
		border:2px solid gray;
		height:500px;
	    float:left;
	    background-image:url(img/天空.jpg);
	    background-repeat:no-repeat;
	    background-attachment:fixed;
	}
	#right{
		width:80%;
		border:2px solid gray;
		height:500px;
		float:right;
	}
	.sec{
	
	}
	#top{
		height:230px;
	}
	#mid{
		height:130px;
	}
	#bel{
		height:130px;
	}
	
	.ge{
		width:140px;
		height:90px;
		border:2px solid #fff;
		border-radius:10px;
	}
	#gezhi1{
		position:relative;
		left:70px;
		bottom:30px
	}
	#gezhi2{
		position:relative;
		left:70px;
		bottom:130px;
	}
	#gezhi3{
		position:relative;
		left:70px;
		bottom:105px;
	}
	.tu{
		width:70px;
		height:70px;
		
	}
	#img1{
		position:relative;
		top:70px;
	}
	#img2{
		position:relative;
		bottom:20px;
		right:10px;
		width:90px;
		height:90px;
	}
	p{
		font-size:25px;
	}
	.zhi{
		width:60px;
		height:30px;

	}
	#zhi1{
		position:relative;
		top:45px;
		left:5px;
	}
	#zhi2{
		position:relative;
		bottom:50px;
		left:5px;
	}
	#zhi3{
		position:relative;
		bottom:30px;
		left:5px;
	}
</style>
</head>
<frameset cols="20%,20%,*">
           <frame frameborder=0 scrolling="no" noresize>
           <frame frameborder=0 src="shuju.html" name="frmleft" scrolling="no" noresize>
	       <frame frameborder=0 src="main.html" name="frmmain" scrolling="no" noresize>
 </frameset>
		<!--<div id="left">
			<div class="sec" id="top">
			      <img class="tu" id="img1" src="img/气体.png">	
			      	<div class="zhi" id="zhi1">
			      		<p>气体</p>
			      	</div>
				<div class="ge" id="gezhi1">
				<p>'''+iterm_all['M']+'''</p>
				</div>
			</div>
			<div class="sec" id="mid">
				<img class="tu" id="img2" src="img/temperature.png">
					<div class="zhi" id="zhi2">
			      		<p>温度</p>
			      	</div>
					<div class="ge" id="gezhi2">
					<p>'''+iterm_all['T']+'''</p>
					</div> 
			</div>
			<div class="sec" id="bel">
				<img class="tu"id="img3" src="img/yyhumidity3.png">
					<div class="zhi" id="zhi3">
			      		<p>湿度</p>
			      	</div>
					<div class="ge" id="gezhi3">
					<p>'''+iterm_all['H']+'''</p>	
					</div>
			</div>
		</div>
		<div id="right">
			<iframe src="">
		</div>-->
</html>
 '''
    with open('./fire.html', 'w+') as fp:
        fp.write(page_now)
    
if __name__ == '__main__':
    while 1:
        getserial()
        print(iterm_all)
        build_page()
        time.sleep(1)
        
        
        


