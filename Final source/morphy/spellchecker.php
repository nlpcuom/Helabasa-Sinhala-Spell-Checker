<?php
ob_start();
ini_set("xdebug.var_display_max_children", -1);
ini_set("xdebug.var_display_max_data", -1);
ini_set("xdebug.var_display_max_depth", -1);
date_default_timezone_set('America/Los_Angeles');


?>

<!doctype html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>හෙළබස - සිංහල අක්ෂර වින්‍යාස සකසනය</title>

  <!-- Bootstrap Core CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

  <!-- Custom Fonts -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

  <link href="vendor/simple-line-icons/css/simple-line-icons.css" rel="stylesheet">

  <!-- Custom CSS -->
  <link href="css/stylish-portfolio.css" rel="stylesheet">

</head>

<body id="page-top">

  <!-- Navigation -->
  <a class="menu-toggle rounded" href="#">
    <i class="fas fa-bars"></i>
  </a>
  <nav id="sidebar-wrapper" class="box-shadows-editor">
    <ul class="sidebar-nav">
      <li class="sidebar-brand">
        <a class="js-scroll-trigger sinhala-f nav-header" href="#page-top">හෙළබස <span class="nav-header-span">v1.1.0</span></a>
      </li>
      <li class="sidebar-nav-item">
        <a class="js-scroll-trigger sinhala-f" href="#page-top">ප්‍රධාන පිටුව</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="js-scroll-trigger sinhala-f" href="#about">අප ගැන තොරතුරු</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="js-scroll-trigger sinhala-f" href="#services">හෙළබස සේවාවන්</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="js-scroll-trigger sinhala-f" href="#portfolio">අපව අමතන්න</a>
      </li>
	  
	  <li class="sidebar-nav-item nav-logo" >
         <img class="img-fluid" src="img/logo.png" alt="Chania" width="460" height="345"> 
      </li>

    </ul>
  </nav>

  <div id="main-page">
  
  
	  <!-- Header -->
	  <section id="start-masthead" class="masthead d-flex">
			  
		
			
			

			<div class="container-fluid " >
			<div class="row justify-content-center m-lg-4 m-sm-1 m-md-1">
				
					<h1 class="mb-1 sinhala-f gray-color-1">හෙළබස</h1>
				
			</div>
			
			<div class="row justify-content-center m-lg-4 m-sm-1 m-md-1">
				
					<h3 class="mb-5 sinhala-f gray-color-2">සිංහල අක්ෂර වින්‍යාස සකසනය</h3>
				
			</div>
			<div class="row justify-content-center m-lg-4 m-sm-1 m-md-1" >
		  
		  
				<div  class="col-lg-8 col-md-12 ">
                    
					<div class="row ">
					
						<div class="col-6 justify-content-start">
							<div class="row justify-content-start ml-1" >
								
								<div class="mb-1 editor-controller-left box-shadow-setting h-100 " style="">
									
									<div class=" h-100 container">
										<div class="row h-100 justify-content-start align-items-center">
											
												<span class=" controller-icon-left rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-placement="top" title="Settings">
													<i class="icon-options"></i>
												</span>
											
												<span class="controller-icon-left rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-placement="top" title="Clear Document" >
													<i class="icon-note"></i>
												</span>

                                                <span class="controller-icon-left rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-placement="top" title="Copy to Clipboard" >
													<i class="icon-docs"></i>
												</span>
											
											
											
										</div>
										
									</div>
								</div>
							</div>
						</div>
						<div class="col-6 ">
							<div class="row justify-content-end mr-1">
								<div class="mb-1 editor-controller-right box-shadow-setting h-100" style="">



                                    <div class=" h-100 container">
                                        <div class="row h-100 justify-content-end align-items-center">


                                            <div   class="engine-status-div mr-1 ml-1 text-center pt-1"  >
                                               <p id="engine-status-text" class="engine-status-p text-light sinhala-f">Engine Status</p>
                                            </div>

											  <div id="engine-icon-d" class="rotate-slow controller-icon-right rounded-circle mr-1 ml-1 text-center pt-1" data-toggle="tooltip" data-placement="top" title="Engine" >
                                                <i id="engine-icon" class=" icon-reload"></i>
                                              </div>




                                        </div>

                                    </div>


                                </div>
							</div>
						</div>
					</div>
					
					<div   class="row ">
						<div id="editor-section" class="col-12">
                            <div id="text-editor-div" class="box-shadow-editor editor-placeholder  editor-wrapper sinhala-f p-3" data-gramm="false" contenteditable="true" spellcheck="false" placeholder="මෙතනින් ලියන්න හෝ වචන පෙළ පේස්ට් කරන්න (CTRL+V)... " ></div>
						</div>
					</div>
					
					
				</div>
				
				<div id="analyzse-section" class=" col-lg-4 col-md-12 d-none d-lg-block" >
                    <div class="col col-12" >
                        <div id="analyze" style="opacity:0.0;border-radius:10px;overflow-wrap: break-word" class="box-shadow-setting bg-light p-2">

                        </div>
                    </div>
				</div>
			
		  </div>
		  
		  
		  
		</div>
		

		
		

			
	  </section>




	  
	</div>





  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded js-scroll-trigger" style="left: 15px !important;right: inherit!important;" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>
  


  <!-- Bootstrap core JavaScript -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>



  <!-- Plugin JavaScript -->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/stylish-portfolio.js"></script>
  <script src="js/xregexp-all.js"></script>

  <script type="text/javascript" charset="UTF-8">

      var isChanging =false;
      var isSpacing =false;
      var isSpanedit =false;
      var isBack =false;
      var isDel =false;
      var isSpanPaste =false;
      var isUniqueWordArrayIsEdditing =false;
	  var isAjaxOnGoing=false;
	  var isHighliting=false;
	  var isMultiline ="MULTI_DIC"; //MULTI_DIC, MULTI_MORPH, SINGLE_MORPH
	  var maxLines =200;

	  




      //Realtime testing paragraph
      var test_para ="";

      function isEmpty(obj) {
          for(let key in obj) {
              if(obj.hasOwnProperty(key))
                  return false;
          }
          return true;
      }


      String.prototype.hexDecode = function(){
          var j;
          var hexes = this.match(/.{1,4}/g) || [];
          var back = "";
          for(j = 0; j<hexes.length; j++) {
              back += String.fromCharCode(parseInt(hexes[j], 16));
          }

          return back;
      }

      String.prototype.hexEncode = function(){
          var hex, i;

          var result = "";
          for (i=0; i<this.length; i++) {
              hex = this.charCodeAt(i).toString(16);
              result += ("000"+hex).slice(-4);
          }

          return result
      }

      function onlyUnique(value, index, self) {
          return self.indexOf(value) === index;
      }


      function moveCaretFromSpan(contentEditableElement,childelement,position)
      {
          console.log("moveCaretFromSpan");
          var range,selection;
          if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
          {
              range = document.createRange();//Create a range (a range is a like the selection but invisible)
              range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              if(position !==0)
              {
                  var children_nid = childelement.id;
                  var children_index = 0;
                  var counter = 0;
                  var child_node_array = contentEditableElement.childNodes;
                  for (const nodei of child_node_array)
                  {

                      if(nodei.nodeName ==="SPAN")
                      {
                          if(children_nid ===nodei.id)
                          {

                              children_index = counter;
                          }
                      }
                      counter++;
                  }
                  if(children_index<counter-1)
                  {
                     if(child_node_array[children_index+1].nodeName ==="#text")
                     {

                         let text_node = document.createTextNode(' ');


                         child_node_array[children_index].parentNode.insertBefore(text_node,child_node_array[children_index].nextSibling);

                         range.setStart(child_node_array[children_index + 1], 1);
                         range.setEnd(child_node_array[children_index + 1], 1);

                     }else
                         {


                             let text_node = document.createTextNode(' ');


                             child_node_array[children_index].parentNode.insertBefore(text_node,child_node_array[children_index].nextSibling);

                             range.setStart(child_node_array[children_index + 1], 1);
                             range.setEnd(child_node_array[children_index + 1], 1);
                         }

                  }
                  else
                  {

                      let text_node = document.createTextNode(' ');


                      child_node_array[children_index].parentNode.insertBefore(text_node,child_node_array[children_index].nextSibling);

                      range.setStart(contentEditableElement.childNodes[children_index+1], 1);
                      range.setEnd(contentEditableElement.childNodes[children_index+1], 1);

                  }

              }
              selection = window.getSelection();//get the selection object (allows you to change selection)
              selection.removeAllRanges();//remove any selections already made
              selection.addRange(range);//make the range you have just created the visible selection
          }
          else if(document.selection)//IE 8 and lower
          {
              range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
              range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              range.select();//Select the range (make it the visible selection
          }
      }

      function moveCaretToSpan(contentEditableElement,childelement,position)
      {
          var range,selection;
          if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
          {
              range = document.createRange();//Create a range (a range is a like the selection but invisible)
              range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              if(position !==0)
              {
                  var children_nid = childelement.id;
                  var children_index = 0;
                  var counter = 0;
                  var child_node_array = contentEditableElement.childNodes;
                  for (const nodei of child_node_array)
                  {

                      if(nodei.nodeName ==="SPAN")
                      {
                          if(children_nid ===nodei.id)
                          {

                              children_index = counter;
                          }
                      }
                      counter++;
                  }
                  if(children_index<counter-1)
                  {
                      if(child_node_array[children_index+1].nodeName ==="#text")
                      {


                          let text_node = document.createTextNode(' ');

                          contentEditableElement.insertBefore(text_node,child_node_array[children_index]);

                          range.setStart(contentEditableElement.childNodes[children_index], 1);
                          range.setEnd(contentEditableElement.childNodes[children_index], 1);

                      }else
                      {


                          let text_node = document.createTextNode(' ');

                          contentEditableElement.insertBefore(text_node,child_node_array[children_index]);

                          range.setStart(contentEditableElement.childNodes[children_index], 1);
                          range.setEnd(contentEditableElement.childNodes[children_index], 1);
                      }

                  }
                  else
                  {
                      let text_node = document.createTextNode(' ');

                      contentEditableElement.insertBefore(text_node,child_node_array[children_index]);

                      range.setStart(contentEditableElement.childNodes[children_index], 1);
                      range.setEnd(contentEditableElement.childNodes[children_index], 1);

                  }

              }
              selection = window.getSelection();//get the selection object (allows you to change selection)
              selection.removeAllRanges();//remove any selections already made
              selection.addRange(range);//make the range you have just created the visible selection
          }
          else if(document.selection)//IE 8 and lower
          {
              range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
              range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              range.select();//Select the range (make it the visible selection
          }
      }


      function getTextNodeIterator(el)
      {
          var document = el.ownerDocument;
          var nodes = [],
              offset = 0,
              node,
              nodeIterator = document.createNodeIterator(el, NodeFilter.SHOW_TEXT, null, false);

          while (node = nodeIterator.nextNode()) {

              nodes.push({
                  textNode: node,
                  start: offset,
                  length: node.nodeValue.length
              });
              offset += node.nodeValue.length;

          }

          return nodes;

      }

      function highlight(element, regex, word,plain_reg,color=0) {

          var document = element.ownerDocument;

          var getNodes = function() {
              var nodes = [],
                  offset = 0,
                  node,
                  nodeIterator = document.createNodeIterator(element, NodeFilter.SHOW_TEXT, null, false);


              while (node = nodeIterator.nextNode()) {


                  if(node.parentElement.tagName !=="SPAN") {

                      nodes.push({
                          textNode: node,
                          start: offset,
                          length: node.nodeValue.length
                      });
                      offset += node.nodeValue.length;
                  }else
                      {
                         if(node.parentElement.id ==="")
                         {

                             nodes.push({
                                 textNode: node,
                                 start: offset,
                                 length: node.nodeValue.length
                             });
                             offset += node.nodeValue.length;


                         }

                      }

              }

              return nodes;
          }




          var nodes = getNodes();

          if (!nodes.length) {
              return;
          }




          var text = "";
          for (var i = 0; i < nodes.length; ++i) {
              text += nodes[i].textNode.nodeValue;

          }
          var match;
		  
		  





          while (match = regex.exec(text)) {
              // Prevent empty matches causing infinite loops

              // console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");
             
			  
			  
		


              if (!match[0].length || match.groups["sin_word"] !==word)
              {
                  regex.lastIndex++;
                  continue;
              }



              // Find the start and end text node
              var startNode = null, endNode = null;
              for (i = 0; i < nodes.length; ++i) {
                  var node = nodes[i];



                  if (node.start + node.length <= match.index +match[0].indexOf(match.groups["sin_word"]) )
                      continue;

                  if (!startNode)
                      startNode = node;

                  if (node.start + node.length >= match.index+match[0].indexOf(match.groups["sin_word"]) + match.groups["sin_word"].length)
                  {
                      endNode = node;
                      break;
                  }
              }



              var range = document.createRange();



              if(startNode ===null || endNode ===null)
              {
                  continue;
              }


              var index_pos =0;
              var last_pos =0;
              var length_diff =0;

              if(match.index ===endNode.start)
              {
                  index_pos = 0+match[0].indexOf(match.groups["sin_word"]);
                  last_pos = index_pos+match.groups["sin_word"].length;
              }else
                  {
                      length_diff = match.index -endNode.start;
                      index_pos=length_diff+match[0].indexOf(match.groups["sin_word"]);
                      last_pos = index_pos+match.groups["sin_word"].length;
                  }

              // if(endNode.textNode.nodeValue.indexOf(match.groups["sin_word"])>0)
              // {
              //     index_pos = endNode.textNode.nodeValue.indexOf(match.groups["sin_word"]);
              // }





              // console.log("<<<<<<<start-node>>>>>>>>");
              // console.log(startNode.textNode.nodeValue);
              // console.log("start-node-index: "+startNode.start)
              // console.log("<<<<<<<end-node>>>>>>>>");
              // console.log(endNode.textNode.nodeValue);
              // console.log("end-node-index: "+endNode.start)
              // console.log("<<<<<<<index>>>>>>>>");
              // console.log("index_pos: "+index_pos);
              // console.log("last_pos: "+(index_pos + match.groups["sin_word"].length));
              // console.log("match index: "+match.index);
              // console.log("text length: "+text.length);
              // console.log("end node length : "+endNode.textNode.nodeValue.length);
              // console.log("length difference: "+(text.length -endNode.textNode.nodeValue.length));
              // console.log("right index : "+match[0].indexOf(match.groups["sin_word"]));


             // range.setStart(startNode.textNode, index_pre);
              if(index_pos >=0){
                    range.setStart(startNode.textNode, index_pos);
              }else
                  {
                      range.setStart(startNode.textNode, startNode.textNode.nodeValue.length+index_pos);
                  }
              range.setEnd(endNode.textNode, last_pos);



              var spanNode = document.createElement("span");
              spanNode.id = generateSPID("s");

			  if(color ==0){
              spanNode.setAttribute("class","wrap-span wrap-span-danger");
			  }
			  else if(color ==1)
			  {
				  spanNode.setAttribute("class","wrap-span wrap-span-warning");
			  }else if(color ==2)
			  {
				  spanNode.setAttribute("class","unicode-wrap wrap-span-unicode");
			  }

              spanNode.appendChild(range.extractContents());
              isHighliting =true;
              range.insertNode(spanNode);
              isHighliting =false;




              nodes = getNodes();
              text = "";
              for (var i = 0; i < nodes.length; ++i) {
                  text += nodes[i].textNode.nodeValue;

              }
          }
		  
		  
		  
				  

      }


      function getCaretCharacterOffsetWithin(element) {
          var caretOffset = 0;
          var doc = element.ownerDocument || element.document;
          var win = doc.defaultView || doc.parentWindow;
          var sel;
          if (typeof win.getSelection != "undefined") {
              sel = win.getSelection();
              if (sel.rangeCount > 0) {



                  var range = win.getSelection().getRangeAt(0);
                  var preCaretRange = range.cloneRange();
                  preCaretRange.selectNodeContents(element);

                  preCaretRange.setEnd(range.endContainer, range.endOffset);
                  caretOffset = preCaretRange.toString().length;



              }
          } else if ((sel = doc.selection) && sel.type != "Control") {
              var textRange = sel.createRange();
              var preCaretTextRange = doc.body.createTextRange();
              preCaretTextRange.moveToElementText(element);
              preCaretTextRange.setEndPoint("EndToEnd", textRange);
              caretOffset = preCaretTextRange.text.length;
          }
          return caretOffset;
      }


      function getCaretCharacterOffsetWithinTest(element) {
          var caretOffset = 0;
          var doc = element.ownerDocument || element.document;
          var win = doc.defaultView || doc.parentWindow;
          var sel;
          if (typeof win.getSelection != "undefined") {
              sel = win.getSelection();
              if (sel.rangeCount > 0) {



                  var range = win.getSelection().getRangeAt(0);

                  var preCaretRange = range.cloneRange();
                  preCaretRange.selectNodeContents(element);

                  preCaretRange.setEnd(range.endContainer, range.endOffset);
                  caretOffset = preCaretRange.toString().length;





              }
          } else if ((sel = doc.selection) && sel.type != "Control") {
              var textRange = sel.createRange();
              var preCaretTextRange = doc.body.createTextRange();
              preCaretTextRange.moveToElementText(element);
              preCaretTextRange.setEndPoint("EndToEnd", textRange);
              caretOffset = preCaretTextRange.text.length;
          }
          return caretOffset;
      }


      function getCaretCharacterOffsetWithinDelete(element) {
          var caretOffset = 0;
          var doc = element.ownerDocument || element.document;
          var win = doc.defaultView || doc.parentWindow;
          var sel;
          if (typeof win.getSelection != "undefined") {
              sel = win.getSelection();
              if (sel.rangeCount > 0) {



                  var range = win.getSelection().getRangeAt(0);
                  var preCaretRange = range.cloneRange();
                  preCaretRange.selectNodeContents(element);
                  preCaretRange.setEnd(range.endContainer, range.endOffset);
                  caretOffset = preCaretRange.toString().length;



              }
          } else if ((sel = doc.selection) && sel.type != "Control") {
              var textRange = sel.createRange();
              var preCaretTextRange = doc.body.createTextRange();
              preCaretTextRange.moveToElementText(element);
              preCaretTextRange.setEndPoint("EndToEnd", textRange);
              caretOffset = preCaretTextRange.text.length;
          }


          return caretOffset;
      }




      function moveCaretMiddleSpan(contentEditableElement,childelement,position,stword,enword)
      {
          var range,selection;
          if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
          {
              range = document.createRange();//Create a range (a range is a like the selection but invisible)
              range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              if(position !==0)
              {
                  var children_nid = childelement.id;
                  var children_index = 0;
                  var counter = 0;
                  var child_node_array = contentEditableElement.childNodes;
                  for (const nodei of child_node_array)
                  {

                      if(nodei.nodeName ==="SPAN")
                      {
                          if(children_nid ===nodei.id)
                          {

                              children_index = counter;
                          }
                      }
                      counter++;
                  }

                  let text_node_space = document.createTextNode(' ');
                  let text_node_stword = document.createTextNode(stword);
                  let text_node_enword = document.createTextNode(enword);
                  console.log("moveCaretMiddleSpan");

                  contentEditableElement.insertBefore(text_node_enword,child_node_array[children_index]);
                  contentEditableElement.insertBefore(text_node_space,text_node_enword);
                  contentEditableElement.insertBefore(text_node_stword,text_node_space);

                  isSpacing = true;
                  contentEditableElement.childNodes[children_index+2].parentNode.removeChild(contentEditableElement.childNodes[children_index+2].nextSibling);

                  range.setStart(contentEditableElement.childNodes[children_index+1], 1);
                  range.setEnd(contentEditableElement.childNodes[children_index+1], 1);






              }
              selection = window.getSelection();//get the selection object (allows you to change selection)
              selection.removeAllRanges();//remove any selections already made
              selection.addRange(range);//make the range you have just created the visible selection
          }
          else if(document.selection)//IE 8 and lower
          {
              range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
              range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              range.select();//Select the range (make it the visible selection
          }
      }



      function moveCaretOnUnSpan(contentEditableElement,childelement,position,innertext,caretlct)
      {
          var range,selection;
          if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
          {
              range = document.createRange();//Create a range (a range is a like the selection but invisible)
              range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start

                  var children_nid = childelement.id;
                  var children_index = 0;
                  var counter = 0;
                  var child_node_array = contentEditableElement.childNodes;
                  for (const nodei of child_node_array)
                  {

                      if(nodei.nodeName ==="SPAN")
                      {
                          if(children_nid ===nodei.id)
                          {

                              children_index = counter;
                          }
                      }
                      counter++;
                  }

                  let text_node_space = document.createTextNode(innertext);


                  isSpanedit = true;
                  contentEditableElement.insertBefore(text_node_space,child_node_array[children_index]);

                  console.log("moveCaretOnUnSpan");
                  contentEditableElement.childNodes[children_index+1].parentNode.removeChild(contentEditableElement.childNodes[children_index].nextSibling);

                  range.setStart(contentEditableElement.childNodes[children_index], caretlct);
                  range.setEnd(contentEditableElement.childNodes[children_index], caretlct);









              selection = window.getSelection();//get the selection object (allows you to change selection)
              selection.removeAllRanges();//remove any selections already made
              selection.addRange(range);//make the range you have just created the visible selection
          }
          else if(document.selection)//IE 8 and lower
          {
              range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
              range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
              range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
              range.select();//Select the range (make it the visible selection
          }
      }

      function getCaretPosition() {
          if (window.getSelection && window.getSelection().getRangeAt) {
              var range = window.getSelection().getRangeAt(0);
              var selectedObj = window.getSelection();
              var rangeCount = 0;
              var childNodes = selectedObj.anchorNode.parentNode.childNodes;
              for (var i = 0; i < childNodes.length; i++) {
                  if (childNodes[i] == selectedObj.anchorNode) {
                      break;
                  }
                  if (childNodes[i].outerHTML)
                      rangeCount += childNodes[i].outerHTML.length;
                  else if (childNodes[i].nodeType == 3) {
                      rangeCount += childNodes[i].textContent.length;
                  }
              }
              return range.startOffset + rangeCount;
          }
          return -1;
      }



      function escapeRegExp(string) {
          return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
      }



      function moveCursorToEnd(id) {
          var p = document.getElementById(id),
              s = window.getSelection(),
              r = document.createRange();

          r.setStart(p, 0);
          r.setEnd(p, 0);
          s.removeAllRanges();
          s.addRange(r);
      }



      function isNumber(str) {

          return !isNaN(str) && !isNaN(parseFloat(str))
      }





      function isDate(str)
      {
          return Date.parse(str);
      }




      function getTextNodesIn(node, includeWhitespaceNodes) {
          var textNodes = [], whitespace = /^\s*$/;

          function getTextNodes(node) {
              if (node.nodeType == 3) {
                  if (includeWhitespaceNodes || !whitespace.test(node.nodeValue)) {
                      textNodes.push(node);
                  }
              } else {
                  for (var i = 0, len = node.childNodes.length; i < len; ++i) {
                      getTextNodes(node.childNodes[i]);
                  }
              }
          }

          getTextNodes(node);
          return textNodes;
      }




      function constructSinhalaWordArray(word,paraID,checking_word_array) {
          if (!isHighliting) {
              var regExRule = /\s*(?<start_part>(–|~|`|!|@|#|$|%|^|&|\*|\(|\)|{|}|\[|\]|;|:|\"|'|<|,|\.|>|\?|\/|\\|\||-|_|\+|=)*)(?<sin_word>[\u0d80-\u0dfe\u200d\u200c\u200b]+)(?<end_part>(~|`|!|@|#|$|%|^|&|\*|\(|\)|{|}|\[|\]|;|:|\"|'|<|,|\.|>|\?|\/|\\|\||-|_|\+|=)*)\s*/g;
              var word_struct = {
                  "input_word": "",
                  "sin_word": "",
                  "start_part": "",
                  "end_part": "",
                  "type": "",
                  "status": "",
                  "c_validity": ""
              };
              var t_SIN = "SIN";
              var t_NUM = "NUM";
              var t_UNK = "UNK";
              var words_to_check = [];
              var input_word = "";

              test_para = paraID;


              let matches_array = [];
              for (const mt of word.matchAll(regExRule)) {
                  matches_array.push(mt);
              }



      

              if (matches_array.length > 0) {

                  if (matches_array.length === 1) {
                      input_word = matches_array[0].input;

                      word_struct["input_word"] = input_word;

                      if (matches_array[0].groups["start_part"] + matches_array[0].groups["sin_word"] + matches_array[0].groups["end_part"] === input_word) {

                          word_struct["sin_word"] = matches_array[0].groups["sin_word"];
                          word_struct["start_part"] = matches_array[0].groups["start_part"];
                          word_struct["end_part"] = matches_array[0].groups["end_part"];
                          word_struct["type"] = "SINHALA_SINGLE_VALID";
                          word_struct["status"] = "WAITING";
                          word_struct["c_validity"] = "PASS";

                          words_to_check.push(word_struct);

                      }
                      else {
                          word_struct["sin_word"] = matches_array[0].groups["sin_word"];
                          word_struct["start_part"] = matches_array[0].groups["start_part"];
                          word_struct["end_part"] = matches_array[0].groups["end_part"];
                          word_struct["type"] = "SINHALA_SINGLE_INVALID";
                          word_struct["status"] = "WAITING";
                          word_struct["c_validity"] = "PASS";

                          words_to_check.push(word_struct);

                      }
                  }
                  else {
                      input_word = matches_array[0].input;
                      let matching_word = "";

                      word_struct["input_word"] = input_word;

                      for (let i = 0; i < matches_array.length; i++) {
                          matching_word = matching_word + matches_array[i].groups["start_part"] + matches_array[i].groups["sin_word"] + matches_array[i].groups["end_part"];

                      }


                      if (input_word === matching_word) {


                          for (let i = 0; i < matches_array.length; i++) {
                              word_struct["sin_word"] = matches_array[i].groups["sin_word"];
                              word_struct["start_part"] = matches_array[i].groups["start_part"];
                              word_struct["end_part"] = matches_array[i].groups["end_part"];
                              word_struct["type"] = "SINHALA_MULTI_VALID";
                              word_struct["status"] = "WAITING";
                              word_struct["c_validity"] = "PASS";

                              words_to_check.push(word_struct);

                          }

                      }
                      else {

                          for (let i = 0; i < matches_array.length; i++) {
                              word_struct["sin_word"] = matches_array[i].groups["sin_word"];
                              word_struct["start_part"] = matches_array[i].groups["start_part"];
                              word_struct["end_part"] = matches_array[i].groups["end_part"];
                              word_struct["type"] = "SINHALA_MULTI_INVALID";
                              word_struct["status"] = "WAITING";
                              word_struct["c_validity"] = "PASS";

                              words_to_check.push(word_struct);

                          }
                      }
                  }


              }
              else {

                  //---> out of SINHALA valid Word --> check for valid numerical word else mark it as a error word

                  if (word !== "") {


                      if (!isNumber(word)) {

                          if (isDate(word)) {

                          }
                          else {



                              //@@@@@@@@@@@@@@@@@@@@@VERY IMPORTANT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                              var con_word;
                              var replace;
                              var re;
                              var tocheck_word;


                              var non_word_check = '[\\W^\\s]';
                              var nwre = new RegExp(non_word_check, "i");
                              var front_idx = 0;
                              var back_idx = word.length;

                              for (let k = 0; k < word.length; k++) {

                                  if (nwre.test(word[k])) {
                                      front_idx += 1;
                                  } else {

                                      break;
                                  }
                              }


                              for (let a = 0; a < word.length; a++) {
                                  if (nwre.test(word[word.length - 1 - a])) {
                                      back_idx -= 1;
                                  } else {

                                      break;
                                  }
                              }


                              if (front_idx === 0 && back_idx === word.length) {
                                  let con_word = escapeRegExp(word);
                                  tocheck_word = word;
                                  replace = '\\b' + con_word + '(?!<\\/span>)\\b';

                                  re = new RegExp(replace, "g");

                              } else {
                                  let con_sub_word = escapeRegExp(word.substring(front_idx, back_idx));
                                  tocheck_word = word.substring(front_idx, back_idx);
                                  replace = '\\b' + con_sub_word + '(?!<\\/span>)\\b';

                                  re = new RegExp(replace, "g");

                              }


                              word_struct["input_word"] = word;
                              word_struct["sin_word"] = tocheck_word;
                              word_struct["start_part"] = "";
                              word_struct["end_part"] = "";
                              word_struct["type"] = "NON_SINHALA_WORD";
                              word_struct["status"] = "WAITING";
                              word_struct["c_validity"] = "PASS";

                              words_to_check.push(word_struct);
                              input_word = word;


                              var paragee = document.getElementById(paraID);

                              //testing purposes only


                              // isChanging = true;
                              // highlight(paragee, re, word,replace);
                              // isChanging = false;


                          }


                      }
                  }

              }


              if (input_word !== "") {
                  if (checking_word_array.hasOwnProperty(paraID)) {

                      if (!checking_word_array[paraID].hasOwnProperty(input_word)) {
                          checking_word_array[paraID][input_word] = words_to_check;
                      }

                  } else {
                      checking_word_array[paraID] = {};

                      checking_word_array[paraID][input_word] = words_to_check;

                  }
              }
          }
      }






      document.querySelector("div[contenteditable]").addEventListener("paste", function(e) {
          isSpacing =true;
          e.preventDefault();
          let text = e.clipboardData.getData("text/plain");
          var text_array_of_paste = text.split("\n");
          var current_span_id;
          var caret_location_on_para;
          var current_para;
          var para_innerHtml;

          var current_para_id;
          var caret_location_on_span;
          var current_span;
          var span_innerHtml;

          for(let o=0;o<e.path.length;o++)
          {
              var idex = e.path[o].id;
              if(idex)
              {

                  if(document.getElementById(idex).classList.contains("wraped-span"))
                  {
                      current_span_id = idex;
                      isSpanPaste =true;
                  }

                  if(document.getElementById(idex).classList.contains("editpara"))
                  {
                      current_para_id= idex;
                      break;
                  }
              }

          }


          if(current_para_id)
          {
              current_para= document.getElementById(current_para_id);
              caret_location_on_para = getCaretCharacterOffsetWithinTest(current_para);
              para_innerHtml = current_para.innerText;

              if(current_span_id)
              {
                  current_span= document.getElementById(current_span_id);
                  caret_location_on_span = getCaretCharacterOffsetWithinTest(current_span);
                  span_innerHtml = current_span.innerText;

                  if(text_array_of_paste.length >=1)
                  {
                      if(text_array_of_paste.length ===1 )
                      {
                          document.execCommand("insertHTML", false, text);
                      }else
                      {

                          console.log("<<<<<<<<<Paragraph>>>>>>>>");
                          console.log(current_para_id);
                          console.log(para_innerHtml);
                          console.log(current_para);
                          console.log(caret_location_on_para);
                          console.log("<<<<<<<<<Span>>>>>>>>");
                          console.log(current_span_id);
                          console.log(span_innerHtml);
                          console.log(current_span);
                          console.log(caret_location_on_span);
                          console.log("<<<<<<<<<Text Paragraph array>>>>>>>>");
                          console.log(text_array_of_paste);


                          //CODE NEED TO BE IMPLEMENTED
                      }
                  }


              }
              else
              {
                  if(text_array_of_paste.length >=1)
                  {
                      if(text_array_of_paste.length ===1 )
                      {
                          document.execCommand("insertHTML", false, text);
                      }else
                          {
                              //CODE NEED TO BE IMPLEMENTED


                              var para_nodes = getTextNodeIterator(current_para);
                              var target_node;
                              var text_count=0;
                              var previous_array=[];
                              var next_array =[];
                              let prev_para_id = current_para_id;

							  


                              if(para_nodes.length >0) {
                                  for (let q = 0; q < para_nodes.length; q++) {
                                      console.log("<<<<<Node>>>>");
                                      console.log("Node Value:"+para_nodes[q].textNode.nodeValue);
                                      console.log("Node Start:"+para_nodes[q].start);
                                      console.log("Node length:"+para_nodes[q].length);
                                      console.log("Caret Location:"+ caret_location_on_para);
                                      console.log("Node end:"+(para_nodes[q].start + para_nodes[q].length));
                                      if (para_nodes[q].start <= caret_location_on_para && caret_location_on_para < (para_nodes[q].start + para_nodes[q].length)) {
                                          console.log(para_nodes[q].textNode.nodeValue);
                                      }

                                  }
                              }else
                                  {
									  
									  
                                      for(let i=0;i<text_array_of_paste.length;i++)
                                      {
                                          if(i===0)
                                          {
                                              current_para.innerText = text_array_of_paste[i];
                                          }else
                                              {

                                                  let uid = generateSPID("p");
                                                  $("#"+prev_para_id).after('<p '+'id=\''+uid+'\' class=\'editpara sinhala-f\'>'+text_array_of_paste[i]+'</p>');

                                                  prev_para_id =uid;


                                              }
                                      }


                                  }
                          }
                  }

              }




          }











      });




      function uniqueArray(value, index, self) {
          return self.indexOf(value) === index;
      }




      Array.prototype.diff = function(a) {
          return this.filter(function(i) {return a.indexOf(i) < 0;});
      };





      function wrapWords(str, tmpl) {
          return str.replace(/\w+/g, tmpl || "<span>$&</span>");
      }



      function generateSPID(first_char) {
          let d = new Date().getTime();
          let d2 = (performance && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
          return first_char+'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
              let r = Math.random() * 16;//random number between 0 and 16
              if(d > 0){//Use timestamp until depleted
                  r = (d + r)%16 | 0;
                  d = Math.floor(d/16);
              } else {//Use microseconds since page-load if supported
                  r = (d2 + r)%16 | 0;
                  d2 = Math.floor(d2/16);
              }
              return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
          });
      }

	$(document).ready(function(){

        var editor_enabled = false;
        var edditor_content = '';
        var paragraph_array ={};
        var checking_word_array ={};
        var words_spelling ={};
		var incorrect_words ={};
		var incorrect_words_checking_pos=0;


	    $('[data-toggle="tooltip"]').tooltip();

        $("#text-editor-div").on("keyup",function (e) {

		

            let p_tag_count = $(this).children("p").length;


            if (e.keyCode === 13 && p_tag_count>0 ) {





                var paras2 = [];


                $("#"+e.target.id).find("p").each(function () {

                    if (!(paras2.includes(this.id))) {
                        paras2.push(this.id);

                    } else {

                        this.id = generateSPID("p");
                        paras2.push(this.id);


                    }

                    let paraid = this.id;

                    var textPara = "";
                    var paragraphEl = document.getElementById(paraid);
                    var paragraphElNodes = paragraphEl.childNodes;

                    for (var z = 0; z < paragraphElNodes.length; z++) {
                        if(paragraphElNodes[z].nodeName  ==="#text")
                        {
                            textPara += paragraphElNodes[z].nodeValue;
                        }

                    }

                    paragraph_array[paraid] = textPara.split(" ").filter(onlyUnique);


                    isUniqueWordArrayIsEdditing =true;
                    for (let jer = 0; jer < paragraph_array[paraid].length; jer++) {

                        constructSinhalaWordArray(paragraph_array[paraid][jer], paraid, checking_word_array);
                    }
                    isUniqueWordArrayIsEdditing =false;

                });

                return false;

            }

            if(p_tag_count===0)
            {

                let uid = generateSPID("p");
                document.execCommand('insertHTML', false, '<p '+'id=\''+uid+'\' class=\'editpara sinhala-f\'><br></p>');

                return false;

            }

        }).on('keydown',  function( e ) {


			

            if(e.keyCode === 46)
            {
                isDel =true;
            }else
                {
                    isDel =false;
                }


            if(e.keyCode === 8)
            {
                isBack =true;
            }else
            {
                isBack =false;
            }





            if(e.keyCode === 32 || e.keyCode === 13 || e.keyCode ===231)
            {

                isSpacing =true;

                if(e.keyCode === 13)
                {
                    isSpacing =false;

                }


            }else
                {
                    isSpacing =false;
                    isSpanedit = false;
                }


        }).on('textInput',  function( e ) {

            var inputdata =e.originalEvent.data;

            var keyCode = inputdata.charCodeAt(inputdata.length-1);

            //
            // console.log(keyCode);
            // console.log(e.originalEvent);

            if(keyCode === 32 || keyCode === 10 )
            {

                isSpacing =true;

                if(keyCode === 10)
                {
                    isSpacing =false;

                }


            }else
            {
                isSpacing =false;
                isSpanedit = false;
            }

        }).on('DOMCharacterDataModified',  function( e ) {


        }).on('DOMSubtreeModified',  function( e ) {

				
				

                if(isChanging ===false && isSpacing ===true) {

				


                    if (e.target.id != "text-editor-div") {
                        <!-- this event listener detect any changes within paragraph -->
							
						
                        if (e.target.id in paragraph_array) {

                            let paraid = e.target.id;

                            var textPara = "";
                            var paragraphEl = document.getElementById(paraid);
                            var paragraphElNodes = paragraphEl.childNodes;

                            for (var z = 0; z < paragraphElNodes.length; z++) {
                                if(paragraphElNodes[z].nodeName  ==="#text")
                                {
                                    textPara += paragraphElNodes[z].nodeValue;
                                }

                            }

                            paragraph_array[paraid] = textPara.split(" ").filter(onlyUnique);
                            isUniqueWordArrayIsEdditing =true;
                            for (let jer = 0; jer < paragraph_array[paraid].length; jer++) {


                                constructSinhalaWordArray(paragraph_array[paraid][jer], paraid, checking_word_array);

                            }
                            isUniqueWordArrayIsEdditing =false;

                        } else {
                            <!-- this detect when span is eddited -->



                            if(e.target.id !=="") {
                                if ($("#" + e.target.id).get(0).tagName === "P") {

                                    let paraid = e.target.id;

                                    var textPara = "";
                                    var paragraphEl = document.getElementById(paraid);
                                    var paragraphElNodes = paragraphEl.childNodes;

                                    for (var z = 0; z < paragraphElNodes.length; z++) {
                                        if(paragraphElNodes[z].nodeName  ==="#text")
                                        {

                                            textPara += paragraphElNodes[z].nodeValue;
                                        }

                                    }

                                    paragraph_array[paraid] = textPara.split(" ").filter(onlyUnique);
                                    isUniqueWordArrayIsEdditing =true;
                                    for (let jer = 0; jer < paragraph_array[paraid].length; jer++) {


                                        constructSinhalaWordArray(paragraph_array[paraid][jer], paraid, checking_word_array);

                                    }
                                    isUniqueWordArrayIsEdditing =false;
                                }
                                else
                                {
                                   if(isSpacing ===true)
                                   {

                                       var el = document.getElementById(e.target.id);
                                       var current_inner_text = e.target.innerText;
                                       var span_length = current_inner_text.length;
                                       var caret_on_span = getCaretCharacterOffsetWithin(el);



                                       if(span_length ===caret_on_span) {


                                           let location = getCaretCharacterOffsetWithin(el.parentElement);

                                           isSpacing =false;
                                           isSpanedit = true;
                                           $("#"+e.target.id).text($("#"+e.target.id).text().trim());
                                           moveCaretFromSpan(el.parentElement,el, location);
                                           isSpanedit = false;


                                       }
                                       else
                                       {
                                           if(caret_on_span ===1) {

                                               let location = getCaretCharacterOffsetWithin(el.parentElement);

                                               isSpacing = false;
                                               isSpanedit = true;
                                               $("#" + e.target.id).text($("#" + e.target.id).text().trim());
                                               moveCaretToSpan(el.parentElement, el, location);
                                               isSpanedit = false;


                                           }else
                                               {
                                                   if(isSpanPaste ===false) {
                                                       var inner_text_array = current_inner_text.split(" ");

                                                       let location = getCaretCharacterOffsetWithin(el.parentElement);

                                                       isSpacing = false;
                                                       isSpanedit = true;
                                                       moveCaretMiddleSpan(el.parentElement, el, location, inner_text_array[0], inner_text_array[inner_text_array.length - 1]);
                                                       isSpanedit = false;

                                                   }else
                                                       {
                                                           moveCaretOnUnSpan(el.parentElement,el, location,current_inner_text,caret_on_span);
                                                           isSpanPaste =false;
                                                       }

                                                   //e.target.outerHTML = e.target.innerHTML
                                               }
                                           //e.target.outerHTML = e.target.innerHTML
                                       }
                                   }
                                   // no need to have else here because only if isSpacing is false this code will get be executed
                                }

                            }
                            else
                            {
                                // No html element which do not have ID; Hence no need to handle here

                            }
                        }

                    }
                    else
                    {
						
						
                        var paras = [];
                        <!-- this event listener detect paragraph adding and removing-->
                        var c = 0;
                        $("#"+e.target.id).find("p").each(function () {


                            if (!(paras.includes(this.id))) {
                                paras.push(this.id);

                            } else {

                                this.id = generateSPID("p");
                                paras.push(this.id);


                            }


                        });


                        if (isEmpty(paragraph_array)) {
							
							

                            for (let i = 0; i < paras.length; i++) {

                                let paraid = paras[i];

                                var textPara = "";
                                var paragraphEl = document.getElementById(paraid);
                                var paragraphElNodes = paragraphEl.childNodes;

                                for (var z = 0; z < paragraphElNodes.length; z++) {
                                    if(paragraphElNodes[z].nodeName  ==="#text")
                                    {
                                        textPara += paragraphElNodes[z].nodeValue;
                                    }

                                }

                                paragraph_array[paraid] = textPara.split(" ").filter(onlyUnique);
                                isUniqueWordArrayIsEdditing =true;
                                for (let jer = 0; jer < paragraph_array[paraid].length; jer++) {


                                    constructSinhalaWordArray(paragraph_array[paraid][jer], paraid, checking_word_array);

                                }
                                isUniqueWordArrayIsEdditing =false;
                            }

                        } else {

								
                            for (let k in paragraph_array) {
								
							
                                if (!(paras.includes(k))) {
									
									
                                    delete paragraph_array[k];
                                    delete checking_word_array[k];
									
                                }
                            }
							
							

                            for (let i = 0; i < paras.length; i++) {

                                let paraid = paras[i];

                                if (!(paraid in paragraph_array)) {

                                    var textPara = "";
                                    var paragraphEl = document.getElementById(paraid);
                                    var paragraphElNodes = paragraphEl.childNodes;

                                    for (var z = 0; z < paragraphElNodes.length; z++) {
                                        if(paragraphElNodes[z].nodeName  ==="#text")
                                        {
                                            textPara += paragraphElNodes[z].nodeValue;
                                        }

                                    }

                                    paragraph_array[paraid] = textPara.split(" ").filter(onlyUnique);
                                    isUniqueWordArrayIsEdditing =true;
                                    for (let ter = 0; ter < paragraph_array[paraid].length; ter++) {


                                        constructSinhalaWordArray(paragraph_array[paraid][ter], paraid, checking_word_array);
                                    }
                                    isUniqueWordArrayIsEdditing =false;
                                }

                            }

                        }

                    }







                }
                else
                {


                    isChanging =true;

                    $("#text-editor-div").find("p").each(function()
                    {
                        $(this).find("span").each(function()
                        {


                            if(this.id )
                            {

                            }else
                            {

                                $(this).contents().unwrap();
                            }

                        });
                    });

                    isChanging =false;




                    if(isSpanedit===false){

                        if( e.target.id !=="" && $("#" + e.target.id).get(0).tagName === "SPAN")
                        {

                            //ZONE RED

                            // console.log("@@@");
                            // console.log("ZONE RED");
                            // console.log("span edit: " +isSpanedit);
                            // console.log("Delete press:  "+isDel);
                            // console.log("Backspace press:   "+isBack);

                            var el = document.getElementById(e.target.id);
                            var current_inner_text = e.target.innerText;
                            var caret_on_span = getCaretCharacterOffsetWithinDelete(el);
                            let location = getCaretCharacterOffsetWithinDelete(el.parentElement);




                            moveCaretOnUnSpan(el.parentElement,el, location,current_inner_text,caret_on_span);


                        }else
                            {
                                //ZONE GREEN






                                // console.log("@@@");
                                // console.log(e.target.id);
                                // console.log("ZONE GREEN");
                                // console.log("span edit: " +isSpanedit);
                                // console.log("Delete press:  "+isDel);
                                // console.log("Backspace press:   "+isBack);


                            }
                    }else
                        {
                            //ZONE YELLOW

                            // console.log("@@@");
                            // console.log("ZONE YELLOW");
                            // console.log("span edit: " +isSpanedit);
                            // console.log("Delete press:  "+isDel);
                            // console.log("Backspace press:   "+isBack);

                        }


                }






        });


        setInterval(function() {



		


            //testing purposes only
            if(test_para !="" && document.getElementById(test_para) && !isAjaxOnGoing) {


				

                if(checking_word_array[test_para] !='undefined' && checking_word_array[test_para] !=null) {

					
					
                    if (Object.keys(checking_word_array[test_para]).length > 0) {

                        if (isMultiline=="MULTI_MORPH") {

                            var len_current_test_para = checking_word_array[test_para].length;
                            var counter =0;
                            var set_array =[];

                            for (var wer in checking_word_array[test_para]) {


                                if (checking_word_array[test_para][wer][0]["status"] === "WAITING" && checking_word_array[test_para][wer][0]["type"] != "NON_SINHALA_WORD" ) {

                                    $("#engine-icon-d").removeClass("rotate-slow");
                                    $("#engine-icon-d").addClass("rotate-fast");$("#engine-icon-d").addClass("bg-success");
                                    $("#engine-icon").removeClass("text-dark");
                                    $("#engine-icon").addClass("text-white");

                                    counter=counter+1;
                                    if(counter <=maxLines) {

                                        set_array.push([wer, checking_word_array[test_para][wer][0]["sin_word"]]);

                                    }else
                                    {
                                        break;
                                    }

                                }else
                                {

                                     $("#engine-icon-d").removeClass("rotate-fast");$("#engine-icon-d").removeClass("bg-success");
                                    $("#engine-icon-d").addClass("rotate-slow");
                                    $("#engine-icon").addClass("text-dark");
                                    $("#engine-icon").removeClass("text-white");

                                }
                            }



                            if(set_array.length >0)
                            {


                                ajaxcallmulti(test_para, set_array);

                            }else
							{
								
								let keysOfedditor = Object.keys(checking_word_array);
								for (let p=0; p<keysOfedditor.length;p++)
								{
									if(keysOfedditor[p] == test_para)
									{
										if (p == keysOfedditor.length-1)
										{
											test_para = keysOfedditor[0];
											break;
										}else
										{
											test_para = keysOfedditor[p+1];
											break;
										}
									}
								}
							}









                        }else if (isMultiline=="MULTI_DIC") {

                            var len_current_test_para = checking_word_array[test_para].length;
                            var counter =0;
                            var set_array =[];

							
							
							
                            for (var wer in checking_word_array[test_para]) {


                                if (checking_word_array[test_para][wer][0]["status"] === "WAITING" && checking_word_array[test_para][wer][0]["type"] != "NON_SINHALA_WORD" ) {

                                    $("#engine-icon-d").removeClass("rotate-slow");
                                    $("#engine-icon-d").addClass("rotate-fast");$("#engine-icon-d").addClass("bg-warning");
									$("#"+test_para).addClass("animate-grad");
									$("#engine-icon").removeClass("text-success");
                                    $("#engine-icon").addClass("text-dark");
                                  

                                    counter=counter+1;
                                    if(counter <=maxLines) {

                                        set_array.push([wer, checking_word_array[test_para][wer][0]["sin_word"]]);

                                    }else
                                    {
                                        break;
                                    }

                                }else
                                {

                             

                                }
                            }



                            if(set_array.length >0)
                            {


                                ajaxcallmultidic(test_para, set_array);

                            }else
							{
								
								let keysOfedditor = Object.keys(checking_word_array);
								for (let p=0; p<keysOfedditor.length;p++)
								{
									if(keysOfedditor[p] == test_para)
									{
										if (p == keysOfedditor.length-1)
										{
											test_para = keysOfedditor[0];
											break;
										}else
										{
											test_para = keysOfedditor[p+1];
											break;
										}
									}
								}
								
								
								        $("#engine-icon-d").removeClass("rotate-fast");$("#engine-icon-d").removeClass("bg-warning");
                                        $("#engine-icon-d").addClass("rotate-slow");
                                        $("#"+test_para).removeClass("animate-grad");
										$("#engine-icon").removeClass("text-dark");
										$("#engine-icon").addClass("text-success");
                                    
								
							}









                        } else if(isMultiline=="SINGLE_MORPH") {




                        for (var wer in checking_word_array[test_para]) {


                            if (checking_word_array[test_para][wer][0]["status"] === "WAITING" && checking_word_array[test_para][wer][0]["type"] != "NON_SINHALA_WORD") {

                                $("#engine-icon-d").removeClass("rotate-slow");
                                $("#engine-icon-d").addClass("rotate-fast");$("#engine-icon-d").addClass("bg-success");
                                $("#engine-icon").removeClass("text-dark");
                                $("#engine-icon").addClass("text-white");


                                ajaxcall(test_para, wer, checking_word_array[test_para][wer][0]["sin_word"]);


                                break;

                            } else {
                                 $("#engine-icon-d").removeClass("rotate-fast");$("#engine-icon-d").removeClass("bg-success");
                                $("#engine-icon-d").addClass("rotate-slow");
                                $("#engine-icon").addClass("text-dark");
                                $("#engine-icon").removeClass("text-white");
                            }
                        }

                    }
                    }

                }


            }else
			{
				if(!(document.getElementById(test_para))){
					delete paragraph_array[test_para];
					delete checking_word_array[test_para];
					
					let keysOfedditor = Object.keys(checking_word_array);
					for (let p=0; p<keysOfedditor.length;p++)
					{
						if(keysOfedditor[p] != test_para)
						{
							test_para = keysOfedditor[p];
							break;
						
						}
					}
				
				}
				
			}



        }, 100);




		function wrapcheckedword_real(test_para,word)
		{
			            //testing purposes only
            if(test_para !="" && document.getElementById(test_para) && word) {

                if(isSpacing) {

                   
                    replace = '(?:^|\\s)(?<start_part>(–|~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?<sin_word>';
                    replace_end= ')(?<end_part>(~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?:^|\\s)';

					
                    replace=replace+word+replace_end;
					
				
					
					
					


                    re = new RegExp(replace, "g");

                    var parageez = document.getElementById(test_para);


                    isChanging = true;
                    highlight(parageez, re, word,replace);
                    isChanging = false;
                }

            }

		}

		function wrapcheckedword_unknown(test_para,word)
		{
			            //testing purposes only
            if(test_para !="" && document.getElementById(test_para) && word) {

                if(isSpacing) {

                   
                    replace = '(?:^|\\s)(?<start_part>(–|~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?<sin_word>';
                    replace_end= ')(?<end_part>(~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?:^|\\s)';

					
                    replace=replace+word+replace_end;
					
				
					
					
					


                    re = new RegExp(replace, "g");

                    var parageez = document.getElementById(test_para);


                    isChanging = true;
                    highlight(parageez, re, word,replace,1);
                    isChanging = false;
                }

            }

		}
		
		function wrapcheckedword_unicode(test_para,word)
		{
			            //testing purposes only
            if(test_para !="" && document.getElementById(test_para) && word) {

                if(isSpacing) {

                   
                    replace = '(?:^|\\s)(?<start_part>(–|~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?<sin_word>';
                    replace_end= ')(?<end_part>(~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?:^|\\s)';

					
                    replace=replace+word+replace_end;
					
				
					
					
					


                    re = new RegExp(replace, "g");

                    var parageez = document.getElementById(test_para);


                    isChanging = true;
                    highlight(parageez, re, word,replace,2);
                    isChanging = false;
                }

            }

		}

        setInterval(function() {


					

            var word_key = Object.keys(incorrect_words)[incorrect_words_checking_pos];
            if(typeof incorrect_words[word_key] !== 'undefined') {
                var word = incorrect_words[word_key]["word"];
            }

			
			if(incorrect_words_checking_pos<Object.keys(incorrect_words).length-1)
			{
				incorrect_words_checking_pos =incorrect_words_checking_pos+1;
			}else
			{
				incorrect_words_checking_pos=0;
			}

	
	

            //testing purposes only
            if(test_para !="" && document.getElementById(test_para) && word) {

				
				

                

					
                   
                    replace = '(?:^|\\s)(?<start_part>(–|~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?<sin_word>';
                    replace_end= ')(?<end_part>(~|`|!|@|#|$|%|^|&|\\*|\\(|\\)|{|}|\\[|\\]|;|:|\\"|\'|<|,|\\.|>|\\?|\\/|\\\\|\\||-|_|\\+|=)*)(?:^|\\s)';

                    replace=replace+word+replace_end;
					
					

                    re = new RegExp(replace, "g");

                    var parageez = document.getElementById(test_para);
					
					
					
			

                    isChanging = true;
					if(incorrect_words[word_key]["suggested"] =="-1")
					{
						highlight(parageez, re, word,replace,1);
					}else if(incorrect_words[word_key]["suggested"] =="-2")
					{
						
						highlight(parageez, re, word,replace,2);
					}
					else
					{
						highlight(parageez, re, word,replace);
					}
                    
                    isChanging = false;
                
				


            }



        }, 100);

        function ajaxcallmulti(para_id,test_array) {
            isAjaxOnGoing =true;
            var correctness="PASS";
            var json_array = JSON.stringify(test_array);

			
            $.ajax({
                url: "/morphy/foma/multiexecute",
                type: "POST", //send it through get method
                dataType:"JSON",
                data: {
                    words: json_array,
                },
                success: function(response) {

				
                    if(response.length>0)
                    {

                        for(let ki=0; ki<response.length;ki++)
                        {

                            if(response[ki][2]=="???")
                            {
                                correctness="FAIL";



                                incorrect_words[response[ki][0]]={"word":response[ki][1],"suggestions":[],"suggested":""};
                                checking_word_array[para_id][response[ki][0]][0]["c_validity"]="FAIL";
                                checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";
                                wrapcheckedword_real(para_id,response[ki][1]);



                            }else
                            {
                                if(response[ki][2]!="EORRO")
                                {
                                        correctness="PASS";
                                        checking_word_array[para_id][response[ki][0]][0]["c_validity"]="PASS";
                                        checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";

                                }


                            }


                        }

                    }


                    isAjaxOnGoing =false;





                },
                error: function(xhr) {
                    correctness="UNK";
                    isAjaxOnGoing =false;
                }
            });

            return correctness;

        }

        function ajaxcallmultidic(para_id,test_array) {
            isAjaxOnGoing =true;
            var correctness="PASS";
            var json_array = JSON.stringify(test_array);

			
            $.ajax({
                url: "/morphy/foma/dicexecute",
                type: "POST", //send it through get method
                dataType:"JSON",
                data: {
                    words: json_array,
                },
                success: function(response) {

					
                    if(response.length>0)
                    {

                        for(let ki=0; ki<response.length;ki++)
                        {

                            if(response[ki][2]=="0")
                            {
                                correctness="FAIL";



                                incorrect_words[response[ki][0]]={"word":response[ki][1],"suggestions":[],"suggested":""};
                                checking_word_array[para_id][response[ki][0]][0]["c_validity"]="FAIL";
                                checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";
                                wrapcheckedword_real(para_id,response[ki][1]);



                            }else
                            {
                                if(response[ki][2]!="EORRO")
                                {
									if(response[ki][2]=="1"){
                                        correctness="PASS";
                                        checking_word_array[para_id][response[ki][0]][0]["c_validity"]="PASS";
                                        checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";
										
									}else if(response[ki][2]=="-1"){
                                        correctness="PASS";
										incorrect_words[response[ki][0]]={"word":response[ki][1],"suggestions":[],"suggested":"-1"};
                                        checking_word_array[para_id][response[ki][0]][0]["c_validity"]="FAIL";
                                        checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";
										wrapcheckedword_unknown(para_id,response[ki][1]);
										
									}else if(response[ki][2]=="-2")
									{
										correctness="PASS";
										incorrect_words[response[ki][0]]={"word":response[ki][1],"suggestions":[],"suggested":"-2"};
                                        checking_word_array[para_id][response[ki][0]][0]["c_validity"]="FAIL";
                                        checking_word_array[para_id][response[ki][0]][0]["status"]="CHECKED";
										wrapcheckedword_unicode(para_id,response[ki][1]);
									}
									
									

                                }


                            }


                        }

                    }


                    isAjaxOnGoing =false;





                },
                error: function(xhr) {
                    correctness="UNK";
                    isAjaxOnGoing =false;
                }
            });

            return correctness;

        }


        function ajaxcall(para_id,word_key,word) {
		  isAjaxOnGoing =true;
          var correctness="PASS";
			
          $.ajax({
              url: "/morphy/foma/execute",
              type: "get", //send it through get method
              data: {
                  word: word,
              },
              success: function(response) {
				  
				 

                  if(response=="???")
                  {
                      correctness="FAIL";

                     

					  incorrect_words[word_key]={"word":word,"suggestions":[],"suggested":""};
					  checking_word_array[para_id][word_key][0]["c_validity"]="FAIL";
					  checking_word_array[para_id][word_key][0]["status"]="CHECKED";
					  wrapcheckedword_real(para_id,word);
					  isAjaxOnGoing =false;
					 
					  
                  }else
                  {
                      correctness="PASS";
					  checking_word_array[para_id][word_key][0]["status"]="CHECKED";
					  isAjaxOnGoing =false;
                  }

              },
              error: function(xhr) {
                  correctness="UNK";
				  isAjaxOnGoing =false;
              }
          });
			
          return correctness;

      }


        $("#text-editor-div").on("click",function (e) {



            let p_tag_count = $(this).children("p").length;
            if($(this).text() ==="" && p_tag_count===0)
            {
                let uid = generateSPID("p");
                $(this).html('<p '+'id=\''+uid+'\' class=\'editpara sinhala-f\'><br></p>');

            }



        });


        $(document).mouseup(function(e)
        {
            let container = $("#text-editor-div");

            let p_tag_count = container.children("p").length;
            if (!container.is(e.target) && container.has(e.target).length === 0 && container.text() ==="" &&p_tag_count<=1)
            {

                container.html("");
            }

            if(container.is(e.target) && p_tag_count===0 && e.which ===3)
            {

                let uid = generateSPID("p");
                container.html('<p '+'id=\''+uid+'\' class=\'editpara sinhala-f\'><br></p>');



            }


        });


		<!-- When start button is pressed -->
	    $(document).on('click', '#start-btn', function() {

	       if(editor_enabled === false)
	       {
               editor_enabled = true;
               $("#start-masthead").html(edditor_content);

           }else
           {
               editor_enabled = false;
               $("#start-masthead").html('');
           }

	    });


        $(document).on('click', '.head-suggestion', function() {

            var spanid = $(this).data("sid");
            var sword = $(this).data("sword");


            isSpacing = false;
            isSpanedit = true;


            $("#"+spanid).text(sword);
            $("#"+spanid).removeClass("wrap-span");
            $("#"+spanid).removeClass("wrap-span-danger");
            $("#"+spanid).addClass("wrap-span-success");

            isSpanedit = false;

            isSpacing = true;

        });


        $(document).on('click', '.unicode-suggestion', function() {

            var spanid = $(this).data("sid");
            var sword = $(this).data("sword");


            isSpacing = false;
            isSpanedit = true;


            $("#"+spanid).text(sword);
            $("#"+spanid).removeClass("unicode-wrap");
            $("#"+spanid).removeClass(" wrap-span-unicode");
            $("#"+spanid).addClass("wrap-span-success");

            isSpanedit = false;

            isSpacing = true;

        });

        $(document).on('click', '.other-suggestion', function() {

            var spanid = $(this).data("sid");
            var sword = $(this).data("sword");


            isSpacing = false;
            isSpanedit = true;


            $("#"+spanid).text(sword);
            $("#"+spanid).removeClass("wrap-span");
            $("#"+spanid).removeClass("wrap-span-danger");
            $("#"+spanid).addClass("wrap-span-success");

            isSpanedit = false;
            isSpacing = true;



        });


        $(document).on('click', '#wadd-btn', function() {

            var word = $(this).data("wider");
			var spanid = $(this).data("sid");


            isSpacing = false;
            isSpanedit = true;

            
			
			
			                $.ajax({
                    url: "foma/addtodic",
                    type: "get", //send it through get method
                    data: "word="+word,

                    success: function(response) {
						if(response =="PASS")
						{
							
							$("#"+spanid).removeClass("wrap-span");
							$("#"+spanid).removeClass("wrap-span-danger");
							$("#"+spanid).removeClass("unicode-wrap");
							$("#"+spanid).removeClass("wrap-span-unicode");
							$("#"+spanid).removeClass("wrap-span-warning");
						}else
						{
							
							
						}

                        
						console.log(response);

                    },
                    error: function(xhr) {

                    }
                });



			
			

            isSpanedit = false;
            isSpacing = true;



        });

        $(document).on('click', '#ignore-btn', function() {


            var spanid = $(this).data("sid");


            isSpacing = false;
            isSpanedit = true;

            $("#"+spanid).removeClass("wrap-span");
            $("#"+spanid).removeClass("wrap-span-danger");
            $("#"+spanid).removeClass("wrap-span-success");
            $("#"+spanid).removeClass("wrap-span-warning");
			$("#"+spanid).removeClass("unicode-wrap");
			$("#"+spanid).removeClass("wrap-span-unicode");

            isSpanedit = false;
            isSpacing = true;




        });


        <!-- When start button is pressed -->
        $(document).on('click', function(e) {

            if(e.target.classList.contains("wrap-span"))
            {
                var targetEle = e.target;
                var targetid = e.target.id;





                var word = targetEle.innerText;

                $("#analyze").html("");
                $("#analyze").animate({
                    opacity: '0.0',
                    height: '100%',
                    width: '100%'
                });
                $("#analyze").html('<img width='+'"200px"'+' src='+'"img/loader.gif"'+' class='+'" mx-auto d-block"'+'>');
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







                        wordrest = '';

                        if(response.length >0){

                            var first_suggestion ="";
                            var rest_suggestions ="";

                            $("#analyze").html("");
                            wordrest=wordrest+'<div class="row ml-2 mb-2 h-100 justify-content-start align-items-center">' +
                                ' <span id="ignore-btn" class="  controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1 " data-toggle="tooltip" data-sid="'+targetid+'" data-placement="top" title="Ignore"> <i class="fas fa-trash-alt"></i> </span>' +
                                ' <span id="undo-btn"  class="controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-sid="'+targetid+'" data-placement="top" title="Undo" > <i class="fas fa-undo "></i> </span>' +
                                ' <span id="wadd-btn"  class="controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-sid="'+targetid+'" data-wider="'+word+'" data-placement="top" title="Add word" > <i class="fas fa-plus-circle "></i> </span>' +
                                ' </div><div class="col-12  ">' +
                                '<hr><p class="analytic-head english-f text-dark" >Suggestions for <kbd class="sinhala-f bg-danger linet text-light">'+word+'</kbd></p> </div>';
                            for(i=0;i<response.length;i++)
                            {

                                if(i==0)
                                {

                                    wordrest =wordrest+'<div class="head-suggestion row justify-content-center m-1 p-1 bg-success" data-sword="'+response[i][0]+'" data-sid="'+targetid+'" style="border-radius:5px">'
                                        +'<div class="col-12 ">'
                                        +'<label  class="'+' analytic-head sinhala-f text-white  '+'"  style="'+''+'">'+response[i][0]+'</label>'
                                        +'</div>'
                                        +'</div>';
                                    first_suggestion = response[i][0];

                                }else if(i<response.length-1)
                                {

                                    wordrest =wordrest+'<div class="other-suggestion row justify-content-center m-1 p-1 bg-secondary" data-sword="'+response[i][0]+'" data-sid="'+targetid+'" style="border-radius:5px">'
                                        +'<div class="col-12 ">'
                                        +'<lable  class="'+' analytic-head sinhala-f text-white '+'"  style="'+''+'">'+response[i][0]+'</lable>'
                                        +'</div>'
                                        +'</div>';

                                    rest_suggestions = rest_suggestions+response[i][0]+"<!>";
                                }else
                                    {

                                        wordrest =wordrest+'<div class="other-suggestion row justify-content-center m-1 p-1 bg-secondary" data-sword="'+response[i][0]+'" data-sid="'+targetid+'" style="border-radius:5px">'
                                            +'<div class="col-12 ">'
                                            +'<lable  class="'+' analytic-head sinhala-f text-white '+'"  style="'+''+'">'+response[i][0]+'</lable>'
                                            +'</div>'
                                            +'</div>';


                                        rest_suggestions = rest_suggestions +response[i][0];
                                    }



                            }




                            $("#analyze").html(wordrest);
                            $('[data-toggle="tooltip"]').tooltip();

                        }else
                        {
                            $("#analyze").html("");
                            $("#analyze").html(
                                '<div class="row justify-content-center m-2 p-2 border border-danger" style="border-radius:5px">'
                                +'<div class="col-12 m-1">'
                                +'<p class="'+'analytic-head sinhala-f text-dark'+'" style="'+''+'">'+'යෝජිත වචන නොමැත!'+'</p>'
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














            } else if (e.target.classList.contains("unicode-wrap"))
			{
				
				var targetEle = e.target;
                var targetid = e.target.id;





                var word = targetEle.innerText;

                $("#analyze").html("");
                $("#analyze").animate({
                    opacity: '0.0',
                    height: '100%',
                    width: '100%'
                });
                $("#analyze").html('<img width='+'"200px"'+' src='+'"img/loader.gif"'+' class='+'" mx-auto d-block"'+'>');
                $("#analyze").animate({
                    opacity: '0.8',
                    height: '100%',
                    width: '100%'
                });

                $.ajax({
                    url: "foma/unicodecheck",
                    type: "get", //send it through get method
                    data: "word="+word,

                    success: function(response) {


                        response=JSON.parse(response.replace(/'/g, '"'));
						wordrest = '';
						  if (response.hasOwnProperty("error")) {
							  
							  if(response["error"] !="0")
							  {
								$("#analyze").html("");
								wordrest=wordrest+'<div class="row ml-2 mb-2 h-100 justify-content-start align-items-center">' +
                                ' <span id="ignore-btn" class="  controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1 " data-toggle="tooltip" data-sid="'+targetid+'" data-placement="top" title="Ignore"> <i class="fas fa-trash-alt"></i> </span>' +
                                ' <span id="undo-btn"  class="controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-sid="'+targetid+'" data-placement="top" title="Undo" > <i class="fas fa-undo "></i> </span>' +
                                ' <span id="wadd-btn"  class="controller-icon-left-f rounded-circle ml-1 mr-1 text-center pt-1" data-toggle="tooltip" data-sid="'+targetid+'" data-wider="'+word+'" data-placement="top" title="Add word" > <i class="fas fa-plus-circle "></i> </span>' +
                                ' </div><div class="col-12  ">' +
                                '<hr><p class="analytic-head english-f text-dark" >Suggestions for <kbd class="sinhala-f bg-danger linet text-light">'+word+'</kbd></p> </div>';
                             
								wordrest=wordrest+'<div class="row justify-content-center m-1 p-1"><div class="col-12" style="padding-left:6px!important"> <p>'
								for (var property in response["word_map"]) {
								
									wordrest=wordrest+'<kbd class="sinhala-f text-dark" style="margin:1px;background-color:'+response["word_map"][property]["color"]+';font-size:20px!important">'+response["word_map"][property]["char"]+'</kbd>'
								}
								wordrest=wordrest+'</p></div></div>'
								 wordrest =wordrest+'<div class="unicode-suggestion  row justify-content-center m-1 p-1 bg-success" data-sword="'+response["cword"]+'" data-sid="'+targetid+'" style="border-radius:5px; margin-left: 14px!important;">'
                                        +'<div class="col-12 ">'
                                        +'<label  class="'+' analytic-head sinhala-f text-white  '+'"  style="'+''+'">'+response["cword"]+'</label>'
                                        +'</div>'
                                        +'</div>';
								$("#analyze").html(wordrest);
								 $('[data-toggle="tooltip"]').tooltip();
								
								
							  }else
							  {
								$("#analyze").html("");
								$("#analyze").html(
									'<div class="row justify-content-center m-2 p-2 border border-danger" style="border-radius:5px">'
									+'<div class="col-12 m-1">'
									+'<p class="'+'analytic-head sinhala-f text-dark'+'" style="'+''+'">'+'යෝජිත වචන නොමැත!'+'</p>'
									+'</div>'
									+'</div>');
							  }
							
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
