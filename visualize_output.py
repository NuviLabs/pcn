import open3d as o3d
import os

folder = "output/pcd/02880940"

for i in sorted(os.listdir(folder)):
    print(i)
    for j in sorted(os.listdir(f"{folder}/{i}")):
        pcd = o3d.io.read_point_cloud(f"{folder}/{i}/{j}")
        o3d.visualization.draw_geometries([pcd])