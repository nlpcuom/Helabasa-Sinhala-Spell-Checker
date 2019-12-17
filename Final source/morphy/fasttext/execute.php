<?php 

ob_start();
ini_set("xdebug.var_display_max_children", -1);
ini_set("xdebug.var_display_max_data", -1);
ini_set("xdebug.var_display_max_depth", -1);
date_default_timezone_set('America/Los_Angeles');


if(isset($_GET))
{
	if(isset($_GET["word"]))
	{
		$word = $_GET["word"];
		
		if($word !="")
		{
			
			$word = rawurldecode($word);
			$commond = "/usr/bin/python3 /var/www/html/morphy/fasttext/client.py ".$word." 2>&1";
			
			

					
			try
			{	
				
				putenv('LANG=en_US.UTF-8'); 
				$result = shell_exec($commond);
				
			
				
				echo($result);
			
				
				
				
				
			}catch(Exception $e)
			{
				
				echo(e);
				
			}

			
			
	
			
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