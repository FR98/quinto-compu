var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'hotmail',
  auth: {
    user: 'francisco-rosal98@hotmail.com',
    pass: ''
  }
});

var mailOptions = {
  from: 'francisco-rosal98@hotmail.com',
  to: 'danieldouma@hotmail.com',
  subject: 'Sending Email using Node.js',
  text: 'Douma Douma Douma'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});