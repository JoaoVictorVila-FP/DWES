// Import statements
package com.example.myothercatalog;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.List;

// Adapter class for the RecyclerView
public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {

    // List of items and other necessary variables
    private final List<MyItem> item_list;
    private final LayoutInflater layoutInflater;
    private final Context context;

    // Constructor to initialize the adapter
    public MyAdapter(List<MyItem> item_list, Context context) {
        this.layoutInflater = LayoutInflater.from(context);
        this.item_list = item_list;
        this.context = context;
    }

    // Inflates the layout for each item in the RecyclerView
    @NonNull
    @Override
    public MyAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = layoutInflater.inflate(R.layout.item_layout, null);
        return new MyViewHolder(view);
    }

    // Binds data to the views in each item of the RecyclerView
    @Override
    public void onBindViewHolder(@NonNull MyAdapter.MyViewHolder holder, int position) {
        MyItem MyItem = item_list.get(position);
        holder.title.setText(MyItem.getTitle());
        Glide.with(context).load(MyItem.getUrl()).into(holder.image);
    }

    // Returns the total number of items in the RecyclerView
    @Override
    public int getItemCount() {
        return item_list.size();
    }

    // ViewHolder class to hold references to the views in each item
    public static class MyViewHolder extends RecyclerView.ViewHolder {

        ImageView image;
        TextView title;

        // Constructor to initialize the ViewHolder
        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            image = itemView.findViewById(R.id.iconImageView);
            title = itemView.findViewById(R.id.cod_title);
        }
    }
}
