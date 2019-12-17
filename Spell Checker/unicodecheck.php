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
		
		$word = rawurldecode($word);
		$commond = "/usr/bin/python3 /var/www/html/morphy/foma/unicode.py '".$word."'";
		
		
	
		putenv('LANG=en_US.UTF-8'); 
		$result = exec($commond);
		
		header('content-type: application/json; charset=UTF-8');
		header('Access-Control-Allow-Origin: *');
		echo(json_encode($result));
		
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