<?php 




if(isset($_GET))
{
	if(isset($_GET["word"]))
	{
		$word = $_GET["word"];
		
		
		
		
		
		
		
		if($word !="")
		{
			$commond = 'foma -l /var/www/html/morphy/foma/sinhala.foma -e up -e '.$word.' -s';
			
			$result =  exec($commond );
			
			
			echo($result);
		}
		else
		{
			echo("EORRO");
		}
		
		
		
	}else
	{
		echo("ERROR");
	}
	
	
	
}else
{
	echo("ERROR");
}







?>