package com.example.tharushashehan.ermsapp04;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONObject;

import java.util.ArrayList;


public class secondActivity extends ActionBarActivity {


    private ListView lstTest01;

    private Button btnSearch;
    private Button btnActivity03;
    private Button btnLogout;

    private LinearLayout layMassage01;
    private LinearLayout layMassage02;
    private LinearLayout layMassage03;
    private LinearLayout layInterview01;
    private LinearLayout layInterview02;
    private LinearLayout layInterview03;

    private TextView txtHomeUpdate;
    private TextView txtAcceptRejectPerson;
    private TextView txtSearchResult;

    private EditText edtSearchQuery;

    boolean acceptOrReject;

    String usernameText ="Tharusha";
    String passwordText = "12";
    String search;
    String acceptOrRejectState;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        lstTest01 = (ListView) findViewById(R.id.lstTest01);

        btnActivity03 = (Button) findViewById(R.id.btnActivity);
        btnSearch =(Button) findViewById(R.id.btnSearch);
        btnLogout =(Button) findViewById(R.id.btnLogout);

        txtHomeUpdate =(TextView) this.findViewById(R.id.txtHomeUpdate);
        txtAcceptRejectPerson =(TextView) this.findViewById(R.id.txtAcceptRejectPerson);
        txtSearchResult =(TextView) this.findViewById(R.id.txtSearchResult);
        edtSearchQuery = (EditText) findViewById(R.id.edtSearchQuery);

        layMassage01 =(LinearLayout) findViewById(R.id.layMassage01);
        layMassage02 =(LinearLayout) findViewById(R.id.layMassage02);
        layMassage03 =(LinearLayout) findViewById(R.id.layMassage03);
        layInterview01 =(LinearLayout) findViewById(R.id.layInterview01);
        layInterview02 = (LinearLayout) findViewById(R.id.layInterview02);
        layInterview03 = (LinearLayout) findViewById(R.id.layInterview03);

        TabHost host = (TabHost)findViewById(R.id.tabHost);
        host.setup();

        //Tab 1
        //TabHost.TabSpec spec = host.newTabSpec("Tab One");
        TabHost.TabSpec tab1 = host.newTabSpec("Tab One");
        tab1.setContent(R.id.layhome);
        tab1.setIndicator("HOME");
        host.addTab(tab1);

        //Tab 2
       // spec = host.newTabSpec("Tab Two");
        TabHost.TabSpec tab2 = host.newTabSpec("Tab Two");
        tab2.setContent(R.id.layaccept);
       // tab2.setContent(new Intent(this, secondActivity.class));
        tab2.setIndicator("MASSAGE");
        host.addTab(tab2);

        //Tab 3
        //spec = host.newTabSpec("Tab Three");
        TabHost.TabSpec tab3 = host.newTabSpec("Tab Three");
        tab3.setContent(R.id.laysearch);
        tab3.setIndicator("SEARCH");
        host.addTab(tab3);

        new ToService01().execute("");
        new YourActivity().onCreate(null);

        btnLogout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),MainActivityLogin.class));
            }
        });


        btnActivity03.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), Actiity03.class));
            }
        });



        //tab 01 layouts work starts here
        layInterview02.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), InterviewRecord.class));
            }
        });
        layInterview01.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), InterviewRecord.class));
            }
        });
        layInterview03.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), InterviewRecord.class));
            }
        });




        //tab 02 layouts work starts here
        layMassage01.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),massageDisplay.class));
            }
        });
        layMassage02.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),massageDisplay.class));
            }
        });
        layMassage03.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),massageDisplay.class));
            }
        });



        //tab 03 button work starts here
        btnSearch.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                search = edtSearchQuery.getText().toString();
                startActivity(new Intent(getApplicationContext(), searchResult.class));

                // new ToService04().execute("");
            }
        });
    }

    private class ToService01 extends AsyncTask<String,String,String> {
        @Override
        protected String doInBackground(String... params) {
            ArrayList content = new ArrayList();
            content = httpManagerJson.getData("http://192.168.56.1:8080/Android/URIParse?name=" + usernameText + "&password=" + passwordText);
            return content.toString();
        }
        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            //txtHomeUpdate.setText(s);
        }
    }

    private class ToService02 extends AsyncTask<String,String,String> {

        @Override
        protected String doInBackground(String... params) {
            String content = HttpManager.getData("http://192.168.56.1:8080/Android/Tab02Parse?name="+acceptOrReject);
            return content;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            txtAcceptRejectPerson.setText(s);
        }
    }

    private class ToService03 extends AsyncTask<String,String,String> {

        @Override
        protected String doInBackground(String... params) {
            String content = HttpManager.getData("http://192.168.56.1:8080/Android/Tab02Parse?result="+acceptOrRejectState);
            return content;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            txtAcceptRejectPerson.setText(s); //txtAcceptRejectPerson
        }
    }


    private class YourActivity extends Activity{
        @Override
        protected void onCreate(Bundle saveInstanceState){
        ArrayAdapter<String> Arr = new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,
                httpManagerJson.getData("http://192.168.56.1:8080/Android/URIParse?name=" + usernameText + "&password=" + passwordText));
        lstTest01.setAdapter(Arr);
        }
    }



    //no need to look at
    /**
    private class ToService04 extends AsyncTask<String,String,String> {

        @Override
        protected String doInBackground(String... params) {
            String content = HttpManager.getData("http://192.168.56.1:8080/Android/Tab03Parse?name="+search);
            return content;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            txtSearchResult.setText(s);
        }


    }


     **/
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_second, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}