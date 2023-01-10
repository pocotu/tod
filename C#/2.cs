using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace CameraExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crea un nuevo objeto de la clase Form
            Form form = new Form();

            // Crea un nuevo objeto de la clase Button
            Button button = new Button();
            button.Text = "Tomar foto";
            button.Location = new Point(10, 10);
            button.Click += new EventHandler(TakePhoto);
            form.Controls.Add(button);

            // Crea un nuevo objeto de la clase PictureBox
            PictureBox pictureBox = new PictureBox();
            pictureBox.Size = new Size(320, 240);
            pictureBox.Location = new Point(10, 50);
            form.Controls.Add(pictureBox);

            // Muestra el formulario
            
        }

        static void TakePhoto(object sender, EventArgs e)
        {
            // Crea un nuevo objeto de la clase OpenFileDialog
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "JPEG Files (*.jpeg)|*.jpeg|PNG Files (*.png)|*.png|JPG Files (*.jpg)|*.jpg|GIF Files (*.gif)|*.gif";
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                // Abre la imagen seleccionada en el PictureBox
                PictureBox pictureBox = (PictureBox)form.Controls[1];
                pictureBox.Image = Image.FromFile(openFileDialog.FileName);
            }
        }
    }
}
