Status: published
Date: 2018-03-06 11:50:03
Author: Jerry Su
Slug: ILB
Title: ILB
Category: 
Tags: 

[TOC]

Defining the 4 Basic Metrics 
 
There are four basic metrics that are important for paid search: impressions, clicks, conversions, and spend. 
An **impression** is a single instance of your ad being displayed when someone types in the search keyword for it.  So you can consider the number of impressions to be roughly the number of people who look at your ad, or at least the number of viewers to whom the ad is served. 
A **click** is an instance of a viewer actually clicking on your ad once it has been displayed.  This is distinct from the number of impressions because it requires that the viewer actually clicks on your ad, not just that your ad is displayed. 
A **conversion** is an instance of a viewer that saw your ad, clicked on it, and took the action you intended for them to take once they got to your landing page.  This action could be downloading an offer, purchasing your product, etc.  When you set up your account, you put some tracking code on your website that lets Google know when someone has completed an offer or bought something, so they can keep track of conversions. 
**Spend** is simply the amount of money that you have spent on your campaign so far


Alexander is a PLA bidding model where we use market feedback to determine how much we are willing to pay per click for each item groups (IG) to hit the target ROAS.  

Data source
The cost per click information for ROAS models can be obtained by developing spark jobs that collect item level cost data from  psdm.ps_pla_prdct_grp and  psdm.pla_item_cost_report.   

Conversion Rate Given Click
We will need to build a model for item-level conversion rate given click. 

But still we need to take into consideration of how much traffic an item will have at the a given bid. 

Item-level Bidding Algorithm
Use bidding from the corresponding item-level group. 
If a conversion model is ready, can use that to decide the bidding. 
Dynamic adjusting of bids. Have some initial bids, monitor impression, click, iGMB, etc. and then adjust based on the observations.


Final Implementation
Decide which ABC to use. In order to do A/B test, we have to choose the 100K items from 1 ABC.

