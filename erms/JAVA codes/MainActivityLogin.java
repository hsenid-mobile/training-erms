package com.example.tharushashehan.ermsapp04;


import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivityLogin extends ActionBarActivity {

    private EditText username,password;
    private Button btnLogin;

    String usernameText,passwordText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_activity_login);

        username = (EditText) findViewById(R.id.edtusername);
        password = (EditText) findViewById(R.id.edtpassword);
        btnLogin = (Button) findViewById(R.id.btnSign);


        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                usernameText = username.getText().toString();
                passwordText = password.getText().toString();

                if (!usernameText.equals("") && !passwordText.equals("")) {
                    new ToService().execute("");
                } else {
                    Toast.makeText(MainActivityLogin.this, "Please Insert Name and password", Toast.LENGTH_LONG).show();
                }
            }
        });
    }
    private class ToService extends AsyncTask<String,String,String> {

        @Override
        protected String doInBackground(String... params) {
            String content = HttpManager.getData("http://192.168.56.1:8080/Android/URLParse?name="+usernameText+"&password="+passwordText);
            return content;}

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            if(s.compareTo("Login Failed")==1){
                Toast.makeText(MainActivityLogin.this, "Login fail", Toast.LENGTH_LONG).show();
            }
           else{
               // startActivity(new Intent(getApplicationContext(), secondActivity.class));
                startActivity(new Intent(getApplicationContext(), JsonTestActivity.class));
            }
        }
    }
}

