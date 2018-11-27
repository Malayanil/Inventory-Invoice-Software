# Inventory-Invoice-Software
<h3>INDEX</h3>
<ol>
  <li>Introduction</li>
  <li>Developed With</li>
  <li>Python External Libraries</li>
  <li>FAQ</li>
  <li>Sample Snapshots and Sample Bill</li>
  <li>NOTE</li>
  </ol>
  <hr>
  <hr>

<h3>1. Introduction</h3>
<p>This is an Inventory Management System tied up with a Invoice Generation System for a store. It can be used for a small convenient store after certain modifications to the GUI. It is a <b>SINGLE USER, HOST ONLY<b> software, not intended for customer use. It has been compiled into a Windows Executable file. The development details are stated below and sample snapshots are on display too.</p>
<hr>
<hr>
<h3>2. Developed with: </h3>
<ul>
  <li>Python 3.7</li>
  <li>SQLite 3</li>
 </ul>
 <hr>
 <hr>
 <h3>3. Python External Libraries Used:</h3>
 <ul>
  <li><b>Python Docs</b>(python-docx): for generation of bills.</li>
  <li><b>SQLite 3</b>(sqlite3): for handling databases. <b>NOTE</b>: The existing sqlite3 library and .dll file given in python has to be updated for use.</li>
  <li><b>CX Freeze</b>(cx_Freeze): for compiling the file into a Windows Executable File (.exe).</li>
 </ul>
 <hr>
 <hr>
 <h3>4. FAQ: What can this software do?</h3>
 <ul>
  <li>It has a GUI Interface for Inventory Management and Invoice Generation of a store, named Daw Bedding Stores.</li>
  <li>It's main window gives the user with 3 choices:
    <ol>
      <li>Generate Bills</li>
      <li>Add to Database</li>
      <li>Update the Database</li>
    </ol>
  <li>The user can run any or all the three instances of the choices together, but it is advisable to do it one at a time.</li>
  <li>Once the user clicks on the "GENERATE BILL" button, the printer connected to the pc or LAN automatically prints the bill and it is also displayed in Microsoft Word (or any other default software to run .doc file). It is also saved in directory named as per the date of use and the files are named according to the customer.</li>
  <li>The software is able to keep on generating invoice and updating the inventory as long as the user wants it to and doesn't need to be restarted every time a customer buys something.</li>
  <li>The software can handle errors like "ITEM OUT OF STOCK", "NO ITEMS WITH SUCH PRODUCT ID" etc and display it to the user for better trouble-shooting.</li>
  </ol>
  <hr>
  <hr>
<h3>5. Sample Snapshots and Sample Bill</h3>
  <p> A few snapshots of the Software in action. I've also uploaded a sample bill which was generated from this software.</p>
  <ul>
  <li>This snapshot shows the Main Window which can be used to run any other process according to user's choice.
    <img src="https://github.com/Malayanil/Inventory-Invoice-Software/blob/master/root_snap.jpg"></li>
  <li>This snapshot shows the Generate Bill's Add to Cart function of the software.
  <img src="https://github.com/Malayanil/Inventory-Invoice-Software/blob/master/add_to_cart_snap.jpg")</li>
  <li>This snapshot shows the Add to Database function of the software.
  <img src="https://github.com/Malayanil/Inventory-Invoice-Software/blob/master/add_to_db_snap.jpg"></li>
  <li>This snapshot shows the Update Database function of the software.
    <img src="https://github.com/Malayanil/Inventory-Invoice-Software/blob/master/update_snap.jpg"></li>
  <li>This snapshot shows the generated bill which has automatically opened in Microsoft Word.
    <img src="https://github.com/Malayanil/Inventory-Invoice-Software/blob/master/bill_snap.jpg"></li>
  </ul>
  <hr>
  <hr>
  <h3>6. NOTE</h3>
  <p>The code for the software has not been uploaded due to privacy and security concerns. Sorry for the inconvenience.<br> The only code-document uploaded is "root.py", only for giving a glimpse of the design of the software. This "root.py" is the main window which invokes the other choices upon being choosed by the user of the software.</p>
  <hr>
  <hr>
