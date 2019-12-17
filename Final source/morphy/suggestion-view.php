<?php

ob_start();
ini_set("xdebug.var_display_max_children", -1);
ini_set("xdebug.var_display_max_data", -1);
ini_set("xdebug.var_display_max_depth", -1);
date_default_timezone_set('America/Los_Angeles');

?>


<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="Helabasa : The Sinhala Suggesion Generator">
  <meta name="author" content="">

  <title>Morphy v1.0.2 - Sinhala Suggesion Generator</title>

  <!-- Bootstrap v4.0 core CSS -->
  <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet">
  <link href="css/custom/morphy_custom.css" rel="stylesheet">
  <link href="css/custom/font-awesome.min.css" rel="stylesheet">

</head>

<body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container">
      <a class="navbar-brand  " href="#" style="font-size:32px" ><strong class="sinhala-f">මොර්</strong><strong class="english-f-lower">phy</strong></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
		  <li class="nav-item m-2">
            <a class="btn btn-sm english-f nav-link" style="font-size:20px" href="/morphy">Morphological Analyzer</a>
          </li>
          <li class="nav-item m-2">
            <a class="btn btn-sm sinhala-f nav-link" style="font-size:20px" href="#">අප ගැන</a>
          </li>
          <li class="nav-item m-2">
            <a class="btn btn-sm btn-warning sinhala-f nav-link text-dark" style="font-size:20px;border-radius:50px;" href="#">අපව අමතන්න <i  id="" class="fa fa-address-card"></i></a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <header class="masthead text-center text-white" style="height:1000px!important;background:#fff!important">
    <div class="masthead-content">
      <div class="container">
        <h1 class="masthead-heading mb-0"><strong class="sinhala-f">සිංහල</strong> </h1>
        <h2 class="masthead-subheading mb-0">Suggesion Generator</h2>

			<div class="row justify-content-center m-2">
				<div class="col col-12" >
					<div class="input-group">
						<input id="word" name="word" type="text" class="sinhala-f bg-white form-control form-control-lg url-field" placeholder="සිංහල වචනය ලියන්න...." value="" autofocus="" style="display:block">
						<span class="input-group-btn">
							<button style="border-bottom-left-radius: 0px;border-top-left-radius: 0px" class="btn btn-lg btn-dark responsive-width" type="submit" id="submit_btn">සොයන්න <i  id="download_btn_i" class="fa fa-gear"></i> </button>
						</span>
					</div>
				</div>
			</div>
			
			<div class="row justify-content-center m-2">
				<div class="col col-12" >
					<div id="analyze" style="opacity:0.0;border-radius:10px;overflow-wrap: break-word" class="border border-secondary bg-light p-2">
			
					</div>
				</div>
			</div>

		

        
      </div>
    </div>
    <div class="bg-circle-1 bg-circle"></div>
    <div class="bg-circle-2 bg-circle"></div>
    <div class="bg-circle-3 bg-circle"></div>
    <div class="bg-circle-4 bg-circle"></div>
  </header>


  <!-- Footer -->
  <footer class="py-5 bg-black">
    <div class="container">
      <p class="m-0 text-center text-white small">Copyright &copy; Morphy 2019</p>
    </div>
    <!-- /.container -->
  </footer>


  <!-- Bootstrap core JavaScript -->
  <script src="js/jquery/jquery.min.js"></script>
  <script src="js/bootstrap/bootstrap.bundle.min.js"></script>

  <!-- custom script -->
  <script type="text/javascript" >
  
  $(document).ready(function () {
		var initiWidth =  $(window).width();
        if(initiWidth < 576 )
        {
            $("#submit_btn").html('<i  id="download_btn_i" class="fa fa-gear"></i>');
        }
        else
        {
            $("#submit_btn").html('සොයන්න <i  id="download_btn_i" class="fa fa-gear"></i>');
        }


        //Change button size when xs
        $(window).on('resize',function(){
            var winWidth =  $(window).width();
            if(winWidth < 576 )
            {
                $("#submit_btn").html('<i  id="download_btn_i" class="fa fa-gear"></i>');
            }
            else
            {
                $("#submit_btn").html('සොයන්න <i  id="download_btn_i" class="fa fa-gear"></i>');
            }
        });
		
		
		
		
		$("#submit_btn").on("click",function(){
			var word =$("#word").val();
			if(word =="")
			{
				$("#word").addClass("border border-danger");
			}else
			{
				
				$("#word").removeClass("border border-danger");
				$("#analyze").html("");	
				$("#analyze").animate({
				  opacity: '0.0',
				  height: '100%',
				  width: '100%'
				});
				$("#analyze").html('<img width='+'"200px"'+' src='+'"img/loader4.gif"'+' class='+'" mx-auto d-block"'+'>');	
				$("#analyze").animate({
				  opacity: '0.8',
				  height: '100%',
				  width: '100%'
				});
								
				$.ajax({
				  url: "fasttext/execute",
				  type: "get", //send it through get method
				  data: "word="+word,
				  
				  success: function(response) {
					
				
					response=JSON.parse(response)
					console.log(response);
					
					
					
					
					
					

					wordrest = '';
					
					if(response.length >0){
						
							$("#analyze").html("");		
							for(i=0;i<response.length;i++)
							{
								
								if(i==0)
								{
									console.log(response[i][0]);
									wordrest =wordrest+'<div class="row justify-content-center m-1 p-1 border border-success" style="border-radius:5px">' 
									+'<div class="col-12 ">'
										+'<p class="'+'analytic-head sinhala-f text-success'+'" style="'+''+'">'+response[i][0]+'</p>'
									+'</div>'
								+'</div>';
									
								}else
								{
									console.log(response[i][0]);
								wordrest =wordrest+'<div class="row justify-content-center m-1 p-1 border border-dark" style="border-radius:5px">' 
									+'<div class="col-12 ">'
										+'<p class="'+'analytic-head sinhala-f text-dark'+'" style="'+''+'">'+response[i][0]+'</p>'
									+'</div>'
								+'</div>';
									
									
								}
													  	
							 
						
							}
							
							$("#analyze").html(wordrest);	

					}else
					{
					  $("#analyze").html("");	
					  $("#analyze").html(
						'<div class="row justify-content-center m-2 p-2 border border-success" style="border-radius:5px">' 
							+'<div class="col-12 m-1">'
								+'<p class="'+'analytic-head sinhala-f text-dark'+'" style="'+''+'">'+'No suggestions'+'</p>'
							+'</div>'
						+'</div>');
						
						
					}
					


						
					 
					 

				  },
				  error: function(xhr) {
					
				  }
				});
				
				
				
						
				$("#analyze").animate({
				  opacity: '1',
				  height: '100%',
				  width: '100%'
				});
				
				
				

				
				
			}
			
			
			
			
		});
	  
  });
  
  </script>



</body>

</html>
