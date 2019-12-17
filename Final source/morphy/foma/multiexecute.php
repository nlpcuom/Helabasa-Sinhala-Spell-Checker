<?php 

ob_start();
ini_set("xdebug.var_display_max_children", -1);
ini_set("xdebug.var_display_max_data", -1);
ini_set("xdebug.var_display_max_depth", -1);
date_default_timezone_set('America/Los_Angeles');



if(isset($_POST))
{
	if(isset($_POST["words"]))
	{
		$words = $_POST["words"];
		$data = json_decode($words,true);
		$arrayis =array();
		
		
		
	
		foreach($data as $word)	{
			
			
			
			
			$word_key =$word[0];
			$wordisd = $word[1];
			
			if($word[1] !="")
			{
				
				//$wordi = rawurldecode($word[1]);
				$wordi = $word[1];
				$commond = 'foma -l /var/www/html/morphy/foma/sinhala.foma -e up -e '.$wordi.' -s';
				
				

						
				try
				{	
					
					//putenv('LANG=en_US.UTF-8'); 
					$result = exec($commond);
					
				
					
					array_push($arrayis,array($word_key,$wordisd,$result)) ;
					

				
					
					
					
					
				}catch(Exception $e)
				{
					
					
					
					array_push($arrayis,array($word_key,$wordisd,"EORRO")) ;
					
				}

				
				
		
				
			}
			else
			{
				array_push($arrayis,array($word_key,$wordisd,"EORRO")) ;
			}
		}
		
		echo(json_encode($arrayis));
		die();
		
		
		
	}else
	{
		echo("1231231");
		die();
	}
	
	
	
}else
{
	echo("asdasd");
	die();
}