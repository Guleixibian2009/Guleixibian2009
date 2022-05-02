#First we want a short description
#Like "SuZhou: ☁️ +13°C"
#Link for this: wttr.in/SuZhou?format=3
shortdescription=`curl -s wttr.in/SuZhou?format=3`
echo $shortdescription
echo "::set-output name=short:${shortdescription}"

#Then we want a longer description
#Link for this: wttr.in/SuZhou?format=j1
longraw=`curl -s wttr.in/SuZhou?format=j1'&'lang=zh`
nowDate=`date '+%Y%m%d'`
nowWeekday=`date '+%w'`
case $nowWeekday in
	0)
	nowWeekday="周日"
	;;
	1)
	nowWeekday="周一"
	;;
	2)
	nowWeekday="周二"
	;;
	3)
	nowWeekday="周三"
	;;
	4)
	nowWeekday="周四"
	;;
	5)
	nowWeekday="周五"
	;;
	6)
	nowWeekday="周六"
	;;
esac
nowWeather=`echo $longraw | jq '. ["current_condition"][0]["lang_zh"][0]["value"]'`
nowTempC=`echo $longraw | jq '. ["current_condition"][0]["temp_C"]'`
sunrise=`echo $longraw | jq '. ["weather"][0]["astronomy"][0]["sunrise"]'`
sunset=`echo $longraw | jq '. ["weather"][0]["astronomy"][0]["sunset"]'`
moonrise=`echo $longraw | jq '. ["weather"][0]["astronomy"][0]["moonrise"]'`
moonset=`echo $longraw | jq '. ["weather"][0]["astronomy"][0]["moonset"]'`
moonPhase=`echo $longraw | jq '. ["weather"][0]["astronomy"][0]["moon_phase"]'`
moonPhase=${moonPhase// /%20}
moonPhase=`curl -s http://fanyi.youdao.com/translate?"&"doctype=json"&"type=AUTO"&"i=${moonPhase:1:${#moonPhase}-2}$moonGraph | jq '. ["translateResult"][0][0]["tgt"]'`
minTempC=`echo $longraw | jq '. ["weather"][0]["mintempC"]'`
maxTempC=`echo $longraw | jq '. ["weather"][0]["maxtempC"]'`
avgTempC=`echo $longraw | jq '. ["weather"][0]["avgtempC"]'`
windDir=`echo $longraw | jq '. ["current_condition"][0]["winddir16Point"]'`
if [[ ${#windDir} = 5 ]]; then
	windDir=${windDir:2:$((${#windDir}-3))}
else
	windDir=${windDir:1:$((${#windDir}-2))}
fi
if [ $windDir = N ]; then
	windDir="北"
elif [ $windDir = NE ]; then
	windDir="东北"
elif [ $windDir = E ]; then
	windDir="东"
elif [ $windDir = SE ]; then
	windDir="东南"
elif [ $windDir = S ]; then
	windDir="南"
elif [ $windDir = SW ]; then
	windDir="西南"
elif [ $windDir = W ]; then
	windDir="西"
elif [ $windDir = NW ]; then
	windDir="西北"
fi
windSpeed=`echo $longraw | jq '. ["current_condition"][0]["windspeedKmph"]'`
if [[ $windSpeed == *.* ]]; then
	windSpeed=${windSpeed%.*}
else
	windSpeed=${windSpeed:1:${#windSpeed}-2}
fi
if [[ $windSpeed -lt 1 ]]; then
	windSpeed="0"
elif [[ $windSpeed -ge 1 ]] && [[ $windSpeed -lt 5 ]]; then
	windSpeed="1"
elif [[ $windSpeed -ge 5 ]] && [[ $windSpeed -lt 11 ]]; then
	windSpeed="2"
elif [[ $windSpeed -ge 11 ]] && [[ $windSpeed -lt 19 ]]; then
	windSpeed="3"
elif [[ $windSpeed -ge 19 ]] && [[ $windSpeed -lt 28 ]]; then
	windSpeed="4"
elif [[ $windSpeed -ge 28 ]] && [[ $windSpeed -lt 38 ]]; then
	windSpeed="5"
elif [[ $windSpeed -ge 38 ]] && [[ $windSpeed -lt 49 ]]; then
	windSpeed="6"
elif [[ $windSpeed -ge 49 ]] && [[ $windSpeed -lt 61 ]]; then
	windSpeed="7"
elif [[ $windSpeed -ge 61 ]]; then
	windSpeed=">7"
fi
cloudCover=`echo $longraw | jq '. ["current_condition"][0]["cloudcover"]'`
chanceRain=`echo $longraw | jq '. ["weather"][0]["hourly"][0]["chanceofrain"]'`
uvIndex=`echo $longraw | jq '. ["weather"][0]["hourly"][0]["uvIndex"]'`
visi=`echo $longraw | jq '. ["weather"][0]["hourly"][0]["visibility"]'`
updateTime=`echo $longraw | jq '. ["current_condition"][0]["localObsDateTime"]'`
long="今天是${nowDate}，${nowWeekday}。现在的天气是${nowWeather:1:${#nowWeather}-2}，${nowTempC:1:${#nowTempC}-2}℃。今天日出${sunrise:1:${#sunrise}-2}，日落${sunset:1:${#sunset}-2}。月出${moonrise:1:${#moonrise}-2}，月落${moonset:1:${#moonset}-2}，月相是${moonPhase:1:${#moonPhase}-2}。今天${minTempC:1:${#minTempC}-2}℃~${maxTempC:1:${#maxTempC}-2}℃，均温${avgTempC:1:${#avgTempC}-2}℃。${windDir}风${windSpeed}级，云度${cloudCover:1:${#cloudCover}-2}%，降雨可能性${chanceRain:1:${#chanceRain}-2}%，紫外线${uvIndex:1:${#uvIndex}-2}级，能见度${visi:1:${#visi}-2}公里。注：wttr.in JSON 更新时间：${updateTime:1:${#updateTime}-2}"
echo $long
echo "::set-output name=long:${long}"

#Next we want a forecast graph
#Link for this: wttr.in/SuZhou.png?lang=zh
graph=`curl -s -o ./dist/weather.png wttr.in/SuZhou.png?lang=zh`