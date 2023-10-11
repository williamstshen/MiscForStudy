//
//  ViewController.swift
//  LandMarks
//
//  Created by Elaina mayo on 2023/10/11.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var tableView: UITableView!
    
    var img_info: [String: [String: Any]] = [
        "Amelia" : ["img" : "amelia.jpg",
                    "description" : "Hololive Mistery detective"],
        "Gura" : ["img" : "gura.jpg",
                 "description" : "Hololive Myth shark"],
        "SakuraMiko" : ["img" : "sakuramiko.jpg",
                 "description" : "Hololive zero Elite"],
        "Koyori" : ["img" : "koyori.jpg",
                 "description" : "Hololive 6th brain"],
        "Suisei" : ["img" : "suisei.jpg",
                 "description" : "Hololive zero singer"],
        "Sora" : ["img" : "tokinosora.jpg",
                 "description" : "Hololive Queen"]
    ]
    var landmarkNames = [String]()
    var landmarkImages = [UIImage]()
    var landmarkDescription = [String]()
    
    var chosenName = ""
    var chosenImage = UIImage()
    var chosenNote = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        tableView.delegate = self
        tableView.dataSource = self
        
        for img_name in Array(img_info.keys) {
            landmarkNames.append(img_name)
            if let img_filename = img_info[img_name]?["img"] as? String {
                landmarkImages.append(UIImage(named:img_filename)!)
            }
            if let img_note = img_info[img_name]?["description"] as? String {
                landmarkDescription.append(img_note)
            }
        }
    }
    
    //[WS] re-define for header errors of protocol UITableViewDelegate and UITableViewDataSource
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        //[WS] return int to show num of rows in table
        return landmarkNames.count
    }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        
        var content = cell.defaultContentConfiguration()
        content.text = landmarkNames[indexPath.row]
        content.secondaryText = landmarkDescription[indexPath.row]
        cell.contentConfiguration = content
        return cell
        
    }
    //[WS] Action when selected : assign value by row index
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        chosenName = landmarkNames[indexPath.row]
        chosenImage = landmarkImages[indexPath.row]
        chosenNote = landmarkDescription[indexPath.row]
        
        performSegue(withIdentifier: "toDetailsVC", sender: nil)
    }
    
    //[WS] called in performSegue (?)
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        if segue.identifier == "toDetailsVC" {
            let destinationVC = segue.destination as! detailsVC
            destinationVC.selectedLandmarkImage = chosenImage
            destinationVC.selectedLandmarkName = chosenName
            destinationVC.selectedLandmarkNote = chosenNote
            
        }
    }
    
    //[WS] monitor swipe gesture (?)
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            self.landmarkNames.remove(at: indexPath.row)
            self.landmarkImages.remove(at: indexPath.row)
            self.landmarkDescription.remove(at: indexPath.row)
            //[WS] not recommended because if thoulands data need to reload
            // tableView.reloadData()
            tableView.deleteRows(at:[indexPath], with: .fade)
        }
    }
}

