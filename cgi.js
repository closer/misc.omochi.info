/* ----------------------------------------------------- */
/* module CGI
/* ----------------------------------------------------- */

var CGI = function(){
  this.params = {
    get : this.get(),
    post : this.post()
  }
};

CGI.prototype.get = function(){
  var get = {};
  if(environment['QUERY_STRING'].length > 0) {
    environment['QUERY_STRING'].split('&').forEach(function(p){
      var arr = p.split(/=/);
      get[arr[0]] = arr[1];
    });
  }
  return get;
}

CGI.prototype.post = function(){
  var post = {};
  var data = readline();
  print(data);
  print(readline());
  if(data.length > 0) {
    data.split('&').forEach(function(p){
      var arr = p.split('=');
      print(p);
      post[arr[0]] = arr[1];
    });
  }
  return post;
}


