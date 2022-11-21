VBR - Creating and Scheduling Backup Jobs
=========================================
To back up VMs, you must configure a backup job. The backup job defines how, where and when to back up VM data.

One job can be used to process one or more VMs. Jobs can be started manually or scheduled to run automatically at a specific time.

Step-By-Step
------------

Create a backup job to protect some of the virtual machines used in the lab environment.

1. Click on HOME workspace, on menu bar, click Backup Job, Virtual Machine, Vmware vSphere

2. At the first step of the wizard, enter Backup (your initials) as the Name. 
Keep the default Description and click Next.
 


3. Click Add… to browse the VI infrastructure to review the selection criteria and select
Veeam-DC01 and Tiny-Veeam. Click Add and Next.


4. Leave Automatic selection for Backup proxy.
5. Confirm Main Backup Repository is selected as Backup repository in the drop down menu.


6. Change the Restore points to keep on disk to 2. 
7. Click Advanced to specify advanced options for the backup job.
8. Leave Incremental selected under Backup mode and click OK and Next.
9. Do not enable synthetic or active full: This way the backup chain will be created in the Forever Forward incremental backup mode. 
   
	
   
10 	 From the Guest OS Credentials dropdown box, choose the Domain Administrator (veeamlab\administrator).. 
11 	Click on the "Applications" button.  Select Tiny-Veeam from the list and click Edit.
12 	Select the Disable application processing radio button. Click OK. And then click OK again. 
Tiny-Veeam is a linux VM so it does not have VSS framework on it, therefore we choose to disable application-aware image processing for this VM.
13 

	   Click Test Now and watch the test complete. Notice that Tiny-Veeam fails guest credentials. That's to be expected and is ok.  

14 	  Click Close as the testing completes.

15 	  Click Next to proceed.

16 	   
  Schedule this job to run daily. Click APPLY to proceed.
  There is no option to schedule the automatic retry for jobs configured to start only manually. 


17 

	 Click Finish
18 	  Click Finish. Feel free to review the job by right clicking and selecting Edit. To keep the lab cleaned up for others, please delete your job when you’re done. 

