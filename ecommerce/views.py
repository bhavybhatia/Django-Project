from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "home_page.html")

def home_page_old(request):
    text = """
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <title>Hello, world!</title>
  </head>

  <body>
  <div class="container">
    <div class="row">
        <div class="col-md-4 col-lg-4 col-xs-4">
    <h1 style="background-color:red;">Hello, world! This is a new line For testing purpose</h1>
    </div>
    <div class="col-md-4 col-lg-4 col-xs-4">
<h1 style="background-color:orange;">Hello, world! Second Div purpose</h1>
</div>
<div class="col-md-4 col-lg-4 col-xs-4">
<h1 style="background-color:blue">Hello, world! This is a Third div purpose</h1>
</div>
    </div>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return HttpResponse(text)
