import Paper from "@mui/material/Paper";
import Typography from "@mui/material/Typography";

import PageContainer from "../components/common/PageContainer";

const DashboardPage = () => {
  return (
    <PageContainer>
      <Paper
        sx={{
          p: 4,
        }}
      >
        <Typography variant="h4">
          Dashboard
        </Typography>

        <Typography sx={{ mt: 2 }}>
          Welcome to Smart Library &
          Book Store
        </Typography>
      </Paper>
    </PageContainer>
  );
};

export default DashboardPage;