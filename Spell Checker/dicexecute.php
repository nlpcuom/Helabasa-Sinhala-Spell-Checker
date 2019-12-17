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
		$data_string = json_encode($data);
		$arrayis =array();
		$data_string_arr = rawurldecode($data_string);
		$data_string_arr =str_replace ("'","&quot;",$data_string_arr);
		
	
		$commond = "/usr/bin/python3 /var/www/html/morphy/foma/client.py '".$data_string_arr."'";
		
		
	
		putenv('LANG=en_US.UTF-8'); 
		$result = exec($commond);
		
		$result = str_replace ("&quot;","'",$result);
		
		echo($result);
		
		
		
		
		
		
		
		
		
		
		die();
		
		/*
		
	
		foreach($data as $word)	{
			
			
			
			
			$word_key =$word[0];
			$wordisd = $word[1];
			
			if($word[1] !="")
			{
				
				$wordi = rawurldecode($word[1]);
				$commond = "/usr/bin/python3 /var/www/html/morphy/foma/client.py ".$wordi."";
				
				

						
				try
				{	
					
					putenv('LANG=en_US.UTF-8'); 
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
		
		*/
		
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