package com.example.myothercatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;


import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;





// Main activity for the application
public class MainActivity extends AppCompatActivity implements select_listener {

    // RecyclerView instance
    private RecyclerView recyclerView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Set the content view for the activity
        setContentView(R.layout.activity_main);

        // Initialize RecyclerView
        recyclerView = (RecyclerView) findViewById(R.id.recyclerview);

        // Make API request to fetch data and populate RecyclerView
        makeRequest();
    }

    // Function to make a request to an API endpoint and populate the RecyclerView
    private void makeRequest() {
        // List to store data from the API response
        List<MyItem> itemList = new ArrayList<>();

        // Create a request to fetch JSON data from the specified URL
        JsonArrayRequest request = new JsonArrayRequest
                (Request.Method.GET,
                        "https://raw.githubusercontent.com/JoaoVictorVila-FP/DWES/main/recursos/catalog.json",
                        null,
                        new Response.Listener<JSONArray>() {
                            @Override
                            public void onResponse(JSONArray response) {
                                try {
                                    // Parse the JSON response and create MyItem objects
                                    for (int i = 0; i < response.length(); i++) {
                                        JSONObject jsonObject = response.getJSONObject(i);
                                        MyItem myItem = new MyItem(jsonObject);
                                        itemList.add(myItem);
                                    }

                                    // Set up the RecyclerView with the populated data
                                    MyAdapter myAdapter = new MyAdapter(itemList, MainActivity.this,MainActivity.this);
                                    recyclerView.setAdapter(myAdapter);
                                    recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));

                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                error.printStackTrace();
                            }
                        }
                );

        // Add the request to the Volley request queue
        Volley.newRequestQueue(this).add(request);
    }


    // En MainActivity.java
    @Override
    public void onItemClick(MyItem myItem) {
        // Crear un nuevo intent para iniciar DetailActivity
        Intent intent = new Intent(MainActivity.this, DetailActivity.class);

        // Obtener los datos de myItem
        String title = myItem.getTitle();
        String url = myItem.getUrl();
        String description = myItem.getDescription();

        // Poner los datos extra en el intent utilizando las claves correctas
        intent.putExtra(DetailActivity.TITLE, title);
        intent.putExtra(DetailActivity.URL, url);
        intent.putExtra(DetailActivity.DESCRIPTION, description);

        // Iniciar DetailActivity
        startActivity(intent);
    }

}
