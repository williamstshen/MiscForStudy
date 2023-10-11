//
//  detailsVC.swift
//  LandMarks
//
//  Created by Elaina mayo on 2023/10/11.
//

import UIKit

class detailsVC: UIViewController {

    @IBOutlet weak var landmarkLabel: UILabel!
    @IBOutlet weak var landmarkImage: UIImageView!
    
    @IBOutlet weak var landmarkNote: UILabel!
    
    var selectedLandmarkName = ""
    var selectedLandmarkNote = ""
    var selectedLandmarkImage = UIImage()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        landmarkLabel.text = selectedLandmarkName
        landmarkImage.image = selectedLandmarkImage
        landmarkNote.text = selectedLandmarkNote
        
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
