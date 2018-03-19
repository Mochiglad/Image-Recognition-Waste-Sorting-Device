const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const AWS = require('aws-sdk');
const fs = require('fs'); //file processing


// load config before setting up AWS services
AWS.config.loadFromPath('config.json');
const recog = new AWS.Rekognition();
const s3 = new AWS.S3(); //amazon cloud storage service


// export modules we need
module.exports.AWS = AWS;
module.exports.recog = recog;
module.exports.fs = fs;


const port = 3000;

app.use(bodyParser.json());

app.use(express.static('./public'));  // this sends clientside files


// starting server
app.listen(port, function(){
    console.log("Server listening on port " + port);
});

app.post('/recogniton', function(request, response){
});

// Call S3 to list current buckets
s3.listBuckets(function(err, data) {
   if (err) {
      console.log("Error", err);
   } else {
      console.log("Bucket List", data.Buckets);
   }
});
