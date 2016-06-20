package com.example.tharushashehan.ermsapp04;

import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ListView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;


public class JsonTestActivity extends ActionBarActivity {

    private TextView txtTest;
    private TextView TxtTest02;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_json_test);

        txtTest = (TextView) findViewById(R.id.txtTest);
        TxtTest02 = (TextView) findViewById(R.id.txtTest02);

        new ToService().execute("");
        new ToService02().execute("");
    }

    private class ToService extends AsyncTask<String, String, String> {

        @Override
        protected String doInBackground(String... params) {

            String content = HttpJsonParser.getData("http://192.168.56.1:8080/Android/URIParse1?name=Tharusha&password=12");
            return content;

        }
            @Override
            protected void onPostExecute(String s) {
                super.onPostExecute(s);
                txtTest.setText(s);
            }
    }
    private class ToService02 extends AsyncTask<String, String, String>{
        @Override
        protected String doInBackground(String... params){
            String content = HttpManager.getData("http://192.168.56.1:8080/Android/Tab03Parse?name=Tharindu");
            return content;
        }
        @Override
        protected void onPostExecute(String s){
            super.onPostExecute(s);
            TxtTest02.setText(s);
            try {
                JSONObject jb = new JSONObject(s);
            } catch (JSONException e) {
                e.printStackTrace();
              //  Log.e("S");
            }
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_json_test, menu);
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
