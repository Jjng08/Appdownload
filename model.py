import os
import instaloader
import re
from pathlib import Path

def descargar_reel(url, output_path):
    try:
        # Si no se especifica output_path, usar la carpeta de Descargas del sistema
        if output_path is None:
            output_path = str(Path.home() / "Downloads" / "InstagramReels")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        pattern = r'instagram.com/reel/([^/]+)'
        match = re.search(pattern, url)
        
        if not match:
            print("URL no válida. Debe ser un reel de Instagram (formato: https://www.instagram.com/reel/CODIGO/)")
            return
            
        shortcode = match.group(1)
        
        
        L = instaloader.Instaloader(
            dirname_pattern=output_path,
            download_pictures=False,    
            download_videos=True,       
            download_video_thumbnails=False,  
            download_geotags=False,     
            download_comments=False,    
            save_metadata=False,
            post_metadata_txt_pattern=''     
        )
        
        
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        
        if not post.is_video:
            print("La URL proporcionada no corresponde a un reel")
            return
            
        print(f"Descargando reel: {post.profile}_{post.shortcode}...")
        
        
        L.download_post(post, target=output_path)
        
        
        old_filename = os.path.join(output_path, f"{post.profile}_{post.shortcode}.mp4")
        new_filename = os.path.join(output_path, f"reel_{post.shortcode}.mp4")
        
        if os.path.exists(old_filename):
            os.rename(old_filename, new_filename)
            print(f"Reel descargado exitosamente como: {new_filename}")
        
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error de Instaloader: {e}")
    except Exception as e:
        print(f"Error al descargar: {e}")

def main():
    url = input("Introduce la URL del reel de Instagram: ")
    output_path = str(Path.home() / "Downloads" / "InstagramReels")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    descargar_reel(url, output_path)

if __name__ == "__main__":
    main()