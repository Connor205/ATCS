<form class="form-target center-confirm" method="POST">
	<input type="hidden" name="csrfmiddlewaretoken" value="Ya4vhG1XuZAnmztJHzLMFdjwmZhItHbsPpWZsExvcPdooKmTceKxWp0q148WcyCI">
	<div class="hero hero--overlap hero--account force-fullwidth text-center text-middle vertical-align">
		<div class="container vertical-align-middle"></div>
	</div>

	<div class="row force-fullwidth">
	<div class="col-md-12 dev_menu">
		<div class="container">
			<div class="row">
				<div class="col-md-3">
					<span class="avatar avatar-online">
	                	<a href="/"><img src="https://avatar.leagueoflegends.com/NA1/Cønn205.png" alt="Cønn205_avatar"></a>
	                </span>
	            </div>

	            <div class="col-md-7" style="margin-top: 20px;">
	                <ul class="nav nav-tabs nav-tabs-line" style="margin-left: -10px;">

		            	<li class="active">
		            		<a href="/">Dashboard</a>
		            	</li>

		            	<li>
		            		<a href="/feed">Feed</a>
		            	</li>

		            	<li>
		            		<a href="/stars">Stars</a>
		            	</li>		            	

		            	<li>
		            		<a href="/following">Following</a>
		            	</li>

		            	<li>
		            		<a href="/followers">Followers</a>
		            	</li>

		            </ul>
		        </div>

		        <div class="col-md-2">
	                <span class="pull-right" style="margin-top:15px;">
	                	<a href="/app-type/" class="btn btn-riot btn-riotred btn-bottom width-200">Register Project</a>
	                </span>
	            </div>
	        </div>
		</div>
	</div>
</div>


	<div class="row ">
		<div class="container info_container">
			
<style>
.btn-riot-sm {
	display: inline-block;
    padding: 0px 8px;
    text-align: center;
    white-space: nowrap;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 3px;
    -webkit-transition: border .2s linear,color .2s linear,width .2s linear,background-color .2s linear;
    -o-transition: border .2s linear,color .2s linear,width .2s linear,background-color .2s linear;
    transition: border .2s linear,color .2s linear,width .2s linear,background-color .2s linear;
    -webkit-font-smoothing: subpixel-antialiased;
	outline: 0;
}
</style>
<div class="row info_row">

	<div class="col-md-3"><h4>Documentation &amp; Policies</h4></div>
	<div class="col-md-9">                        
		<p>We suggest reading through our documentation before working with the Riot Games API.<br>
        Every project owner is expected to adhere to the documentation and policies. Failure<br>
            to adhere to the documentation or policies can lead to the revocation of API access.</p>

        <p><a href="/getting-started.html"><b>Getting Started</b></a> · <a href="/policies.html"><b>Policies</b></a> · <a href="/rate-limiting.html"><b>Rate Limiting</b></a> · <a href="/application-process.html"><b>Application Process</b></a></p>
	</div>
</div>

<hr style="margin:20px;">

<div class="row info_row">
	<div class="col-md-3"><h4>Development API Key</h4></div>
	<div class="col-md-9">
        <p>This API key is to be used for development only. Please register any permanent projects.<br>
		<b>Do NOT use this API key in a publicly available project!</b></p>

		

		<p class="row" style="margin: 0 0 11px;">
			<input id="apikey" type="password" style="width: 350px; padding: 1px 5px; margin-left:-5px; letter-spacing: -1.25px; border: 1px solid rgb(169, 169, 169);" value="RGAPI-6e2c8adb-e70c-480f-9070-348ab3f71f60" readonly="">
			<button id="apikey_show" type="button" class="btn-riot-sm btn-riotred" style="height: 26px;">Show</button>
			<button id="apikey_copy" type="button" class="btn-riot-sm btn-riot" style="height: 26px;">Copy</button>
		</p>

		<p>
		
            
                <b>Expires:
            
            Fri, Nov 2nd, 2018 @ 10:03am (PT) in 1 hour and 23 minutes</b>
        

   		
        </p>

	</div>
</div>

<script>
let apiKey = $("#apikey");

$("#apikey_show").click(function() {
    if (apiKey.attr("type") == "password") {
        apiKey.attr("type", "text");
        apiKey.css("letter-spacing", "0px");
        $(this).html("Hide");
	} else {
        apiKey.attr("type", "password");
        apiKey.css("letter-spacing", "-1.25px");
        $(this).html("Show");
	}
});

$("#apikey_copy").click(function() {
    copyTextToClipboard(apiKey.val());
    $(this).html("Copied");
    setTimeout(function() {$("#apikey_copy").html("Copy");}, 5000);
});
</script>

<hr style="margin:20px;">

<div class="row info_row">
	<div class="col-md-3"><h4>Rate Limits</h4></div>
	<div class="col-md-9">
		
		<p>
		  	
		  		20 requests every 1 seconds<br>
		  	
		  		100 requests every 2 minutes<br>
		  	
	  	</p>

	  	<p>Note that rate limits are enforced per region. For example, with the above rate limit, you could make 20 requests every 1 seconds to both NA and EUW endpoints simultaneously.</p>
	  	
	</div>
</div>

<div class="row info_row">
	<div class="col-md-3"></div>
	<div class="col-md-9">
		<div class="g-recaptcha" data-sitekey="6LcOGicUAAAAAI8bWJ6IYXt5teyzO-t4aKskR5Iz"><div style="width: 304px; height: 78px;"><div><iframe src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LcOGicUAAAAAI8bWJ6IYXt5teyzO-t4aKskR5Iz&amp;co=aHR0cHM6Ly9kZXZlbG9wZXIucmlvdGdhbWVzLmNvbTo0NDM.&amp;hl=en&amp;v=v1540794797339&amp;size=normal&amp;cb=l4oqdwbuf54f" width="304" height="78" role="presentation" name="a-826w2t3dxjcf" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox"></iframe></div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div>
		<div style="margin-top: 25px;">
		<input type="submit" name="confirm_action" class="btn btn-riot btn-riotred btn-bottom width-200" value="Regenerate API Key">
		<a href="/app/352836/usage" class="btn btn-riot">View API Key Usage</a>
		</div>
	</div>
</div>
		</div>
	</div>
</form>