package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    public static final String TITLE = "TITLE";
    public static final String URL = "URL";
    public static final String DESCRIPTION = "DESCRIPTION";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        ImageView imageView = findViewById(R.id.imageView); // Make sure you have an ImageView with this ID in your layout
        TextView titleView = findViewById(R.id.titleTextView); // Make sure you have a TextView with this ID in your layout
        TextView descriptionView = findViewById(R.id.descriptionTextView); // Make sure you have a TextView with this ID in your layout

        // Extract data from the Intent
        String title = getIntent().getStringExtra(TITLE);
        String url = getIntent().getStringExtra(URL);
        String description = getIntent().getStringExtra(DESCRIPTION);

        // Update views with the received data
        Glide.with(this).load(url).into(imageView);
        titleView.setText(title);
        descriptionView.setText(description);
    }
}
