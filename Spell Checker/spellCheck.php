<?php 

ob_start();
ini_set("xdebug.var_display_max_children", -1);
ini_set("xdebug.var_display_max_data", -1);
ini_set("xdebug.var_display_max_depth", -1);
date_default_timezone_set('America/Los_Angeles');

$response = array();

if(isset($_GET))
{
	if(isset($_GET["word"]))
	{
		$word = $_GET["word"];
		$dataArr =array(array($word,$word));
		$data_string = json_encode($dataArr);
		$data_string_arr = rawurldecode($data_string);
		$data_string_arr =str_replace ("'","&quot;",$data_string_arr);
		
		$commond = "/usr/bin/python3 /var/www/html/morphy/foma/client.py '".$data_string_arr."'";
		
		putenv('LANG=en_US.UTF-8'); 
		$result = exec($commond);
		
		$result = str_replace ("&quot;","'",$result);
		
		$response['response_code'] = 200;
		$response['response_data'] = json_decode($result);

	}else
	{
		$response['response_code'] = 404;
		$response['response_data'] = 'Not Input Data Found!';
	}
	
}else
{
	$response['response_code'] = 404;
	$response['response_data'] = 'Request method Mismatched!';
}


header('content-type: application/json; charset=UTF-8');
header('Access-Control-Allow-Origin: *');
echo(json_encode($response, JSON_PRETTY_PRINT));
