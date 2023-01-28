<?php

  switch ($_REQUEST["operation"]) {

    case "length": 
       $lat=$_GET['lat'];
	   if ($lat==null) $lat=0;
	   if ($lat>90 or $lat<-90){
			echo "ERROR !!!";
			echo "<br>";
			echo "Latitude must be between -90 to 90 degrees.";
			break;
			}
	   $result=round(2*M_PI*6371*cos(deg2rad($lat)),2);
	   echo "&ltlatitude&gt";
 	   echo "$lat";
       echo "&lt/latitude&gt";
	   echo "<br>";
	   echo "&ltlength&gt";
 	   echo "$result";
       echo "&lt/length&gt";
       echo "<br>";
       break;

    default:
		echo "This WEB SERVICE was developed using PHP language.";
        echo "<br>";
		echo "It provides one operation:";
		echo "length";
		echo "(input parameter: lat)";
		echo "<br>";
		echo "<br>";
		echo "...the operation provides THE LENGTH IN KILOMETERS OF ANY PARALLEL IN XML FORMAT, based on the input parameter lat (latitude) in the format +DD.dddd.";
		echo "<br>";
		echo "<br>";
		echo "The calculation assumes the Earth spherical and with radius of 6,371 km.";
		echo "<br>";
		echo "<br>";
		echo "Syntax example: http://gaia.gge.unb.ca:8080/gge5403/labs/3/parallel.php?operation=length&lat=45";
    }

?>