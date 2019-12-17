<?php 




if(isset($_GET))
{
	if(isset($_GET["word"]))
	{
		$word = $_GET["word"];
		
		
		
		
		
		
		
		if($word !="")
		{
		
			
			$myfile = file_put_contents('dic.txt', $word.PHP_EOL , FILE_APPEND | LOCK_EX);
			
			if($myfile)
			{
				echo("PASS");
			}else
			{
				echo("EORRO");
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
